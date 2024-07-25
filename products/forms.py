from django import forms
from .models import Property

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'location', 'category', 'photo']



class GeneralSearchForm(forms.Form):
    value = forms.CharField(required=False)