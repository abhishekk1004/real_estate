from django import forms
from .models import Payment, Invoice

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['property', 'amount', 'service_charge']



class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        widgets = {
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'payment': forms.Select(attrs={'class': 'form-control'}),
        }