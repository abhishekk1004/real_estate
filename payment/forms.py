from django import forms
from .models import Payment, Invoice

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['file']
