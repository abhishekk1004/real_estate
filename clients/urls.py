from django.urls import path
from . import views

urlpatterns = [
    path('favorite/', views.save_favorite_property, name='save_favorite_property'),
    path('inquiry/', views.make_inquiry, name='make_inquiry'),
    path('upload/<int:pk>/', views.upload_document, name='upload_document'),
    path('request/', views.request_viewing, name='request'),
]
