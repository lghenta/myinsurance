from django.db import models

class Contact(models.Model):
    """Model representing a contact."""
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        """String representation of the Contact object."""
        return self.name

class HubSpotContact(models.Model):
    """Model representing a contact in HubSpot."""
    hubspot_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        """String representation of the HubSpotContact object."""
        return f"{self.first_name} {self.last_name}"

class OAuthCredentials(models.Model):
    """Model representing OAuth credentials."""
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    access_token = models.CharField(max_length=512, null=True, blank=True)
    token_type = models.CharField(max_length=20, null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    refresh_token = models.CharField(max_length=512, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the OAuthCredentials object."""
        return f"OAuth Credentials for Client ID: {self.client_id}"

class APICallResult(models.Model):
    """Model representing the result of an API call."""
    timestamp = models.DateTimeField(auto_now_add=True)
    endpoint = models.CharField(max_length=255)
    response_data = models.TextField()
    status_code = models.IntegerField()
    successful = models.BooleanField(default=False)

    def __str__(self):
        """String representation of the APICallResult object."""
        return f"{self.endpoint} - Success: {self.successful} - Status: {self.status_code} - Time: {self.timestamp}"
