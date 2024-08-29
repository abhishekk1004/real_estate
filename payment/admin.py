from django.contrib import admin
from .models import Payment, Invoice, Receipt, InvoiceItem

# Register your models here.


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('client', 'property', 'amount', 'service_charge', 'created_at')
    search_fields = ('client__username', 'property__title')
    list_filter = ('created_at',)

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [InvoiceItemInline]

admin.site.register(Invoice, InvoiceAdmin)

@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('receipt_number', 'invoice', 'issued_at')
    search_fields = ('receipt_number', 'invoice__invoice_number')
    list_filter = ('issued_at',)
