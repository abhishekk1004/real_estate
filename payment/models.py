from django.db import models
from django.contrib.auth import get_user_model
from products.models import Property
from datetime import timedelta
from django.utils import timezone

User = get_user_model()

class Payment(models.Model):
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id} by {self.client.username}"

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True)
    company_name = models.CharField(max_length=255, default="Default Company Name")
    company_address = models.TextField(default="Default Address")
    company_email = models.EmailField(default="default@example.com")
    client_name = models.CharField(max_length=255, default="Unknown")
    client_address = models.TextField(max_length=255, null=True, blank=True)
    client_email = models.EmailField(default="example@example.com")
    invoice_date = models.DateField(default=timezone.now)
    due_date = models.DateField(default=timezone.now)
    vat_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)

    def calculate_vat_due(self):
        return self.calculate_subtotal() * (self.vat_rate / 100)
    
    def calculate_subtotal(self):
        return sum(item.calculate_total() for item in self.items.all())

    def calculate_total_due(self):
        return self.calculate_subtotal() + self.calculate_vat_due()

    def __str__(self):
        return f"Invoice {self.invoice_number}"
    
    

class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, related_name='items', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField(default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_total(self):
        return self.quantity * self.unit_price

    def __str__(self):
        return f"{self.description} ({self.quantity} x {self.unit_price})"

class Receipt(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    receipt_number = models.CharField(max_length=12, unique=True)
    issued_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.receipt_number
