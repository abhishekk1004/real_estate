from django.db import models
from clients.models import Client
from products.models import Property

# Create your models here.

class Payment(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    property = models.ForeignKey('products.Property', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE)
    file = models.FileField(upload_to='invoices/')
    generated_at = models.DateTimeField(auto_now_add=True)


