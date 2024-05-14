from django.core.management.base import BaseCommand
from contacts.models import Contact  # replace with your actual model
import requests

class Command(BaseCommand):
    help = 'Exports contacts to HubSpot'

    def handle(self, *args, **options):
        contacts = Contact.objects.all()
        url = 'https://api.hubapi.com/crm/v3/objects/contacts'
        headers = {
            'Authorization': 'Bearer CK_rhaD3MRIHAAEAQAAAARjIuf1EIPu-2R8ojv3KATIU2Q7BUFW4TNFkI6H62V6aAvKvYwQ6MAAAAEEAAAAAAAAAAAAAAAAAgAAAAAAAAAAAACAAAAAAAOABAAAAAAAAAAAAAAAQAkIUqRLN-g02CviQXGT2iNZZ3TJgpEFKA2V1MVIAWgBgAA',
            'Content-Type': 'application/json'
        }

        for contact in contacts:
            data = {
                "properties": {
                    "email": contact.email,
                    "firstname": contact.first_name,
                    "lastname": contact.last_name,
                    # add other fields as needed
                }
            }
            response = requests.post(url, json=data, headers=headers)
            if response.status_code == 201:
                self.stdout.write(self.style.SUCCESS(f"Successfully exported contact {contact.email}"))
            else:
                self.stdout.write(self.style.ERROR(f"Failed to export contact {contact.email}: {response.text}"))
