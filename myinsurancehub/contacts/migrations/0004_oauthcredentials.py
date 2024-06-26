# Generated by Django 5.0.6 on 2024-05-13 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_hubspotcontact_alter_hubspotcredentials_client_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthCredentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255)),
                ('client_secret', models.CharField(max_length=255)),
                ('access_token', models.CharField(blank=True, max_length=512, null=True)),
                ('token_type', models.CharField(blank=True, max_length=20, null=True)),
                ('expires_in', models.IntegerField(blank=True, null=True)),
                ('refresh_token', models.CharField(blank=True, max_length=512, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
