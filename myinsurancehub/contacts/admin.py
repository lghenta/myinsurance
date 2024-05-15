from django.contrib import admin
from .models import Contact, HubSpotContact, OAuthCredentials, APICallResult

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Admin configuration for Contact model."""
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(HubSpotContact)
class HubSpotContactAdmin(admin.ModelAdmin):
    """Admin configuration for HubSpotContact model."""
    list_display = ('first_name', 'last_name', 'email', 'phone')
    search_fields = ('first_name', 'last_name', 'email')

@admin.register(OAuthCredentials)
class OAuthCredentialsAdmin(admin.ModelAdmin):
    """Admin configuration for OAuthCredentials model."""
    list_display = ('client_id', 'last_updated')
    readonly_fields = ('last_updated',)

@admin.register(APICallResult)
class APICallResultAdmin(admin.ModelAdmin):
    """Admin configuration for APICallResult model."""
    list_display = ('endpoint', 'timestamp', 'successful', 'status_code')
    list_filter = ('successful', 'timestamp')
    search_fields = ('endpoint',)
