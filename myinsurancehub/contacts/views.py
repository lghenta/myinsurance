from django.shortcuts import redirect, render
from django.urls import reverse
import requests
from .models import OAuthCredentials, APICallResult

def hubspot_auth(request):
    """
    Initiates the OAuth2 authentication process with HubSpot.
    Redirects the user to HubSpot for authorization.
    """
    credentials = OAuthCredentials.objects.first()
    if not credentials or not credentials.client_id:
        return render(request, 'error.html', {'message': 'OAuth Credentials not found.'})
    
    redirect_uri = 'http://localhost:8000' + reverse('hubspot_callback')
    scopes = "crm.objects.contacts.read crm.objects.contacts.write"
    auth_url = f"https://app.hubspot.com/oauth/authorize?client_id={credentials.client_id}&redirect_uri={redirect_uri}&scope={scopes}&response_type=code"
    return redirect(auth_url)

def hubspot_callback(request):
    """
    Handles the callback from HubSpot after the user authorizes the application.
    Exchanges the authorization code for an access token and saves it.
    """
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

def fetch_contacts(url, access_token):
    """
    Fetches contacts from HubSpot API using the provided URL and access token.
    Returns the response JSON data or None if unsuccessful.
    """
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(url, headers=headers)
    APICallResult.objects.create(
        endpoint=url,
        response_data=response.text,
        status_code=response.status_code,
        successful=response.ok
    )
    return response.json() if response.status_code == 200 else None

def contact_list(request):
    """
    Fetches a list of contacts from the HubSpot API.
    Renders the contact list page with the retrieved contacts.
    """
    credentials = OAuthCredentials.objects.first()
    if credentials and credentials.access_token:
        url = 'https://api.hubapi.com/crm/v3/objects/contacts'
        contacts_data = fetch_contacts(url, credentials.access_token)
        if contacts_data:
            contacts = contacts_data.get('results', [])
            return render(request, 'contacts/contact_list.html', {'contacts': contacts})
        else:
            return render(request, 'error.html', {'message': 'Failed to fetch contacts from HubSpot.'})
    return render(request, 'error.html', {'message': 'No valid access token.'})

def home(request):
    """
    Serves as the homepage of the application.
    Fetches contacts from HubSpot and renders the homepage with the retrieved contacts.
    """
    credentials = OAuthCredentials.objects.first()
    if credentials and credentials.access_token:
        url = 'https://api.hubapi.com/crm/v3/objects/contacts'
        contacts_data = fetch_contacts(url, credentials.access_token)
        if contacts_data:
            contacts = contacts_data.get('results', [])
            return render(request, 'contacts/homepage.html', {'contacts': contacts})
    return render(request, 'error.html', {'message': 'No valid access token.'})
