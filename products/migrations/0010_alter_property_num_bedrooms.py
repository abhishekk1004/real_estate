# Generated by Django 5.0.7 on 2024-07-21 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_property_num_bedrooms_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='num_bedrooms',
            field=models.IntegerField(),
        ),
    ]
