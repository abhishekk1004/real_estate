from django.db import models
from accounts.models import User



# Create your models here.

class Property(models.Model):
    RENT = 'rent'
    SALE = 'sale'
    LEASE = 'lease'
    
    CATEGORY_CHOICES = [
        (RENT, 'Rent'),
        (SALE, 'Sale'),
        (LEASE, 'Lease'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    agent = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': User.AGENT})
    photo = models.ImageField(upload_to='property_photos/')
    city = models.CharField(max_length=50, default='Default City')
    square_feet = models.IntegerField(default= 100)
    num_bedrooms = models.IntegerField()
    num_floors = models.IntegerField(default=1)



