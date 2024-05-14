from django.shortcuts import redirect, render
from django.urls import reverse
from .models import OAuthCredentials, APICallResult, Contact, HubSpotContact
import requests

def hubspot_auth(request):
    credentials = OAuthCredentials.objects.first()
    if not credentials or not credentials.client_id:
        return render(request, 'error.html', {'message': 'OAuth Credentials not found.'})
    redirect_uri = 'http://localhost:8000' + reverse('hubspot_callback')
    scopes = "crm.objects.contacts.read crm.objects.contacts.write"
    auth_url = f"https://app.hubspot.com/oauth/authorize?client_id={credentials.client_id}&redirect_uri={redirect_uri}&scope={scopes}&response_type=code"
    return redirect(auth_url)

def hubspot_callback(request):
    code = request.GET.get('code')
    credentials = OAuthCredentials.objects.first()
    redirect_uri = 'http://localhost:8000' + reverse('hubspot_callback')
    token_url = 'https://api.hubapi.com/oauth/v1/token'
    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    })
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

def contact_list(request):
    credentials = OAuthCredentials.objects.first()
    if credentials and credentials.access_token:
        headers = {'Authorization': f'Bearer {credentials.access_token}'}
        url = 'https://api.hubapi.com/crm/v3/objects/contacts'
        response = requests.get(url, headers=headers)
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
    credentials = OAuthCredentials.objects.first()
    if credentials and credentials.access_token:
        headers = {'Authorization': f'Bearer {credentials.access_token}'}
        response = requests.get('https://api.hubapi.com/crm/v3/objects/contacts', headers=headers)
        contacts = response.json().get('results', [])
        return render(request, 'contacts/homepage.html', {'contacts': contacts})
    return render(request, 'error.html', {'message': 'No valid access token.'})


