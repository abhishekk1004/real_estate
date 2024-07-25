from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ADMIN = 'admin'
    AGENT = 'agent'
    CLIENT = 'client'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (AGENT, 'Agent'),
        (CLIENT, 'Client'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)