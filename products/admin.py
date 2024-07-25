from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Property

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'agent', 'price', 'city', 'category')
    list_filter = ('category', 'city', 'agent')
    search_fields = ('title', 'description', 'city', 'location')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'agent', 'price','city', 'photo', 'location', 'square_feet', 'num_bedrooms', 'num_floors', 'category')
        }),
    )

admin.site.register(Property, ProductAdmin)
