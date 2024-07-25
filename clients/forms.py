from django import forms
from .models import Inquiry, Document, Appointment

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['message']



class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['file']


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_time']