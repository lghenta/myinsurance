from django.db import models

class HubSpotCredentials(models.Model):
    client_id = models.CharField(max_length=255, default='b4e6aa6c-f0d2-4e63-99b5-6b6eeffec4bd')
    client_secret = models.CharField(max_length=255, default='e671619f-9d9e-4d23-8f71-f85df6bd3d48')
    access_token = models.CharField(max_length=512, blank=True, null=True)

    def __str__(self):
        return "HubSpot Credentials"

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name

class HubSpotContact(models.Model):
    hubspot_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OAuthCredentials(models.Model):
    client_id = models.CharField(max_length=255)
    client_secret = models.CharField(max_length=255)
    access_token = models.CharField(max_length=512, null=True, blank=True)  # You might include refresh tokens if applicable
    token_type = models.CharField(max_length=20, null=True, blank=True)
    expires_in = models.IntegerField(null=True, blank=True)
    refresh_token = models.CharField(max_length=512, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OAuth Credentials for Client ID: {self.client_id}"

class APICallResult(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    endpoint = models.CharField(max_length=255)
    response_data = models.TextField()
    status_code = models.IntegerField()
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.endpoint} - Success: {self.successful} - Status: {self.status_code} - Time: {self.timestamp}"




