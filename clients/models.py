from django.db import models
from accounts.models import User
from products.models import Property

# Create your models here.



class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_properties = models.ManyToManyField('products.Property', related_name='favorited_by')

#inquiry view
class Inquiry(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey('products.Property', on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

#Document Views
class Document(models.Model):
    property = models.ForeignKey('products.Property', on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Appointment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey('products.Property', on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('scheduled', 'Scheduled'), ('completed', 'Completed'), ('cancelled', 'Cancelled')])

    def __str__(self):
        return f"Appointment with {self.client} for {self.property}"