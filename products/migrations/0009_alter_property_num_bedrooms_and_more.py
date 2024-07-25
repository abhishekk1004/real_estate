# Generated by Django 5.0.7 on 2024-07-21 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_property_num_bedrooms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='num_bedrooms',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='num_floors',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='property',
            name='square_feet',
            field=models.IntegerField(default=100),
        ),
    ]
