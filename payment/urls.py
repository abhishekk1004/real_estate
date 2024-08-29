from django.urls import path
from . import views

urlpatterns = [
    path('create_invoice/<int:payment_id>/', views.create_invoice, name='create_invoice'),
    path('invoice_detail/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('list/', views.invoice_list, name='invoice_list'),
    path('print/<int:invoice_id>/', views.print_invoice, name='print_invoice'),
]
