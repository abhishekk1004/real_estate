from django.urls import path
from . import views

urlpatterns = [
    path('properties/', views.property_list, name='property_list'),
    path('properties/add/', views.add_property, name='add_property'),
    path('properties/<int:property_id>/', views.property_detail, name='property_detail'),
    path('properties/<int:property_id>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('properties/<int:property_id>/enquiry/', views.make_enquiry, name='make_enquiry'),
    path('favorites/', views.favorite_properties, name='favorite_properties'),
    path('remove_fav/<int:property_id>/', views.remove_favorite, name='remove_favorite'),
    path('clients/<int:client_id>/', views.client_details, name='client_details'),
    path('clients/<int:client_id>/interactions/', views.client_interactions, name='client_interactions'),
    path('clients/<int:client_id>/track_interaction/', views.track_interaction, name='track_interaction'),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('header/', views.header, name='header'),
    path('contact/', views.contact, name='contact'),
    path('service/', views.service, name='service'),
    path('blog/', views.blog, name='blog'),
]
