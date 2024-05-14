from django.contrib import admin
from .models import Contact
from .models import HubSpotContact
from .models import OAuthCredentials
from .models import APICallResult

admin.site.register(Contact)


class HubSpotContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'phone']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['first_name', 'last_name']

admin.site.register(HubSpotContact, HubSpotContactAdmin)

class OAuthCredentialsAdmin(admin.ModelAdmin):
    list_display = ['client_id', 'last_updated']
    readonly_fields = ['last_updated']

admin.site.register(OAuthCredentials, OAuthCredentialsAdmin)

@admin.register(APICallResult)
class APICallResultAdmin(admin.ModelAdmin):
    list_display = ('endpoint', 'timestamp', 'successful', 'status_code')
    list_filter = ('successful', 'timestamp')
    search_fields = ('endpoint',)



