# Generated by Django 5.0.6 on 2024-05-13 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_hubspotcredentials'),
    ]

    operations = [
        migrations.CreateModel(
            name='HubSpotContact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hubspot_id', models.CharField(max_length=255, unique=True)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='hubspotcredentials',
            name='client_id',
            field=models.CharField(default='b4e6aa6c-f0d2-4e63-99b5-6b6eeffec4bd', max_length=255),
        ),
        migrations.AlterField(
            model_name='hubspotcredentials',
            name='client_secret',
            field=models.CharField(default='e671619f-9d9e-4d23-8f71-f85df6bd3d48', max_length=255),
        ),
    ]