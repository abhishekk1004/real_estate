# Generated by Django 5.0.7 on 2024-07-31 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_client_appointment_favorite_inquiry'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='additional_files',
            field=models.FileField(blank=True, null=True, upload_to='property_files/'),
        ),
    ]
