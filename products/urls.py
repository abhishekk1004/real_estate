from django.urls import path
from . import views

urlpatterns = [
    path('list', views.property_list, name='property_list'),
    path('details/', views.property_detail, name='property_detail'),
    path('add/', views.property_add, name='property_add'),
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('header', views.header, name='header'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('blog', views.blog, name='blog'),
]
