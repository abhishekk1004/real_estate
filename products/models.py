from django.db import models
from accounts.models import User
from django.conf import settings



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
    photo = models.ImageField(upload_to='property_images/')
    city = models.CharField(max_length=50, default='Default City')
    square_feet = models.IntegerField(default= 100)
    num_bedrooms = models.IntegerField(default= 1)
    num_floors = models.IntegerField(default=1)
    agent = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    pass
    @property
    def is_favorite(self):
        return self.favorite_set.filter(user=self.request.user).exists()
    

    



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_properties = models.ManyToManyField('products.Property', related_name='favorited_by')



class Favorite(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorite_properties')


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey('products.Property', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Appointment with {self.client} for {self.property}"


# For enquiry
class Inquiry(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, default='Default Name')
    email = models.EmailField(default='default@example.com')
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"Inquiry from {self.name} for {self.property.title}"

# For Intereaction
class ClientInteraction(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    interaction_type = models.CharField(max_length=100)
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Interaction with {self.client} on {self.date}"
    



