from django import forms
from .models import Property, Inquiry, ClientInteraction

class PropertyForm(forms.ModelForm):
    class Meta:
        model = Property
        fields = ['title', 'description', 'price', 'photo', 'location', 
            'city', 'num_bedrooms', 'num_floors', 'square_feet']
        

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['name', 'email', 'phone', 'message']



class GeneralSearchForm(forms.Form):
    value = forms.CharField(required=False)


class InteractionForm(forms.ModelForm):
    class Meta:
        model = ClientInteraction
        fields = ['interaction_type', 'notes']


class ReplyForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Your Reply')