from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Payment, Invoice, Receipt
from .forms import PaymentForm, InvoiceForm
import uuid
from products.models import Property

def is_client(user):
    return user.is_authenticated and user.role == 'client'

@login_required
@user_passes_test(is_client)
def create_invoice(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            invoice = form.save(commit=False)
            invoice.property = property
            invoice.client = request.user
            invoice.total_amount = property.price + invoice.service_charge
            invoice.save()
            return redirect('invoice_detail', invoice_id=invoice.id)
    else:
        form = InvoiceForm()
    return render(request, 'payment/create_invoice.html', {'form': form, 'property': property})

@login_required
@user_passes_test(is_client)
def invoice_detail(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'payment/invoice_detail.html', {'invoice': invoice})

@login_required
@user_passes_test(is_client)
def issue_receipt(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    receipt = Receipt.objects.create(
        invoice=invoice,
        receipt_number=str(uuid.uuid4()).replace('-', '')[:12]
    )
    return render(request, 'payment/receipt_detail.html', {'receipt': receipt})

@login_required
@user_passes_test(is_client)
def invoice_list(request):
    invoices = Invoice.objects.filter(client=request.user)
    return render(request, 'payment/invoice_list.html', {'invoices': invoices})

@login_required
@user_passes_test(is_client)
def print_invoice(request, invoice_id):
    invoice = get_object_or_404(Invoice, id=invoice_id)
    return render(request, 'payment/print_invoice.html', {'invoice': invoice})