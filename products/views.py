from django.shortcuts import render, redirect
from .models import *
from .forms import PropertyForm
from django.contrib.auth.decorators import login_required, user_passes_test



# Create your views here.


def property_list(request):
    properties = Property.objects.all()
    return render(request, 'product_list.html', {'properties': properties})

def property_detail(request, pk):
    property = Property.objects.get(pk=pk)
    return render(request, 'product_detail.html', {'property': property})

def property_add(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user
            property.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def is_agent(user):
    return user.is_authenticated and user.role == 'agent'

@login_required
@user_passes_test(is_agent)
def add_property(request):
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.agent = request.user  # Assuming agent is the logged-in user
            property.save()
            return redirect('property_list')
    else:
        form = PropertyForm()
    return render(request, 'add_property.html', {'form': form})


def home(request):    
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def header(request):
    return render(request, 'header.html')


def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

def blog(request):
    return render(request, 'blog.html')