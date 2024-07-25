from django.shortcuts import render, redirect
from .models import Client, Inquiry, Property, Document, Appointment
from .forms import InquiryForm, DocumentForm, AppointmentForm

# Create your views here.



def save_favorite_property(request, pk):
    property = Property.objects.get(pk=pk)
    client = Client.objects.get(user=request.user)
    client.favorite_properties.add(property)
    return redirect('property_detail', pk=pk)

def make_inquiry(request, pk):
    property = Property.objects.get(pk=pk)
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.client = client
            inquiry.property = property
            inquiry.save()
            return redirect('property_detail', pk=pk)
    else:
        form = InquiryForm()
    return render(request, 'inquiries/inquiry.html', {'form': form})


def upload_document(request, pk):
    property = Property.objects.get(pk=pk)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.property = property
            document.save()
            return redirect('property_detail', pk=pk)
    else:
        form = DocumentForm()
    return render(request, 'inquiries/document_form.html', {'form': form})


def request_viewing(request, pk):
    property = Property.objects.get(pk=pk)
    client = Client.objects.get(user=request.user)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.client = client
            appointment.property = property
            appointment.save()
            return redirect('property_detail', pk=pk)
    else:
        form = AppointmentForm()
    return render(request, 'appointment_form.html', {'form': form})