from django.core.management.base import BaseCommand
from contacts.models import OAuthCredentials

class Command(BaseCommand):
    help = 'Adds initial OAuth credentials to the database'

    def handle(self, *args, **options):
        OAuthCredentials.objects.create(
            client_id='your-client-id',
            client_secret='your-client-secret'
        )
        self.stdout.write(self.style.SUCCESS('Successfully added OAuth credentials.'))
