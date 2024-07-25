from django.urls import path
from . import views

urlpatterns = [
    path('make/<int:pk>/', views.make_payment, name='make_payment'),
    path('invoice/<int:payment_id>/', views.generate_invoice, name='generate_invoice'),
]
