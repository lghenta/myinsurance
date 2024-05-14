from .models import Contact
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import HubSpotCredentials, HubSpotContact
import requests
from .models import OAuthCredentials, APICallResult

def hubspot_auth(request):
    credentials = HubSpotCredentials.objects.first()
    redirect_uri = 'http://localhost:8000' + reverse('hubspot_callback')
    # Including multiple scopes in the URL
    scopes = "crm.objects.contacts.read%20crm.objects.contacts.write"
    auth_url = f"https://app.hubspot.com/oauth/authorize?client_id={credentials.client_id}&redirect_uri={redirect_uri}&scope={scopes}&response_type=code"
    return redirect(auth_url)


def hubspot_callback(request):
    code = request.GET.get('code')
    credentials = HubSpotCredentials.objects.first()
    redirect_uri = 'http://localhost:8000' + reverse('hubspot_callback')
    token_url = 'https://api.hubapi.com/oauth/v1/token'
    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    })

    # Log the token exchange attempt
    APICallResult.objects.create(
        endpoint=token_url,
        response_data=response.text,
        status_code=response.status_code,
        successful=response.status_code == 200
    )

    if response.status_code == 200:
        credentials.access_token = response.json().get('access_token')
        credentials.save()
        return redirect('home')
    else:
        return render(request, 'error.html', {'message': 'Failed to get access token.'})


def make_api_call(endpoint):
    response = requests.get(endpoint)
    try:
        APICallResult.objects.create(
            endpoint=endpoint,
            response_data=response.text,
            status_code=response.status_code,
            successful=response.ok
        )
    except Exception as e:
        # Handle possible exceptions that could occur during save
        print(f"Failed to save API call result: {str(e)}")

    return response


def contact_list(request):
    credentials = HubSpotCredentials.objects.first()
    if credentials and credentials.access_token:
        headers = {'Authorization': f'Bearer {credentials.access_token}'}
        url = 'https://api.hubapi.com/crm/v3/objects/contacts'
        response = requests.get(url, headers=headers)

        # Log the API call
        APICallResult.objects.create(
            endpoint=url,
            response_data=response.text,
            status_code=response.status_code,
            successful=response.ok
        )

        if response.status_code == 200:
            contacts = response.json().get('results', [])
            return render(request, 'contacts/contact_list.html', {'contacts': contacts})
        else:
            return render(request, 'error.html', {'message': 'Failed to fetch contacts from HubSpot.'})

    return render(request, 'error.html', {'message': 'No valid access token.'})


def home(request):
    credentials = HubSpotCredentials.objects.first()
    if credentials and credentials.access_token:
        headers = {'Authorization': f'Bearer {credentials.access_token}'}
        response = requests.get('https://api.hubapi.com/crm/v3/objects/contacts', headers=headers)
        contacts = response.json().get('results', [])
        return render(request, 'contacts/homepage.html', {'contacts': contacts})
    return render(request, 'error.html', {'message': 'No valid access token.'})

def fetch_hubspot_contacts(request):
    credentials = OAuthCredentials.objects.first()
    if credentials and credentials.access_token:
        headers = {
            'Authorization': f'Bearer {credentials.access_token}',
            'Content-Type': 'application/json'
        }
        hubspot_url = 'https://api.hubapi.com/crm/v3/objects/contacts'

        # Making the API call
        response = requests.get(hubspot_url, headers=headers)
        
        # Log the API call result
        APICallResult.objects.create(
            endpoint=hubspot_url,
            response_data=response.text,
            status_code=response.status_code,
            successful=response.status_code == 200
        )

        if response.status_code == 200:
            hubspot_contacts = response.json().get('results', [])
            return render(request, 'contacts/contact_list.html', {'hubspot_contacts': hubspot_contacts})
        else:
            return render(request, 'error.html', {'message': 'Failed to fetch contacts from HubSpot.'})

    return render(request, 'error.html', {'message': 'No valid access token.'})




