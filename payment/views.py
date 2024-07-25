from django.shortcuts import render, redirect
from .models import Payment, Invoice, Property, Client
from .forms import PaymentForm, InvoiceForm

# Create your views here.

def make_payment(request, pk):
    property = Property.objects.get(pk=pk)
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.client = client
            payment.property = property
            payment.save()
            return redirect('property_detail', pk=pk)
    else:
        form = PaymentForm()
    return render(request, 'payments/payment_form.html', {'form': form})

def generate_invoice(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, request.FILES)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.payment = payment
            invoice.save()
            return redirect('payment_detail', payment_id=payment_id)
    else:
        form = InvoiceForm()
    return render(request, 'payments/invoice_form.html', {'form': form})