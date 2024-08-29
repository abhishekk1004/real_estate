from django.shortcuts import render, redirect, get_object_or_404
from .models import Property, Favorite, Client, ClientInteraction, Inquiry
from .forms import PropertyForm, InquiryForm, InteractionForm, ReplyForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db.models import Q
from django.contrib import messages
from payment.models import Invoice

# Check if user is an agent
def is_agent(user):
    return user.is_authenticated and user.role == 'agent'

# Check if user is a client
def is_client(user):
    return user.is_authenticated and user.role == 'client'


@login_required
@user_passes_test(is_agent)
def clients_list(request):
    clients = Client.objects.all()
    return render(request, 'inquiries/client_list.html', {'clients': clients})


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
    return render(request, 'agent/create_property.html', {'form': form})

@login_required
def property_list(request):
    query = request.GET.get('q')
    properties = Property.objects.all()
    zip_code = request.GET.get('zip_code')
    city = request.GET.get('city')
    address = request.GET.get('address')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if query:
        properties = properties.filter(
            Q(title__icontains=query) | 
            Q(city__icontains=query) | 
            Q(price__icontains=query) | 
            Q(address__icontains=query) | 
            Q(description__icontains=query)
        )
    if zip_code:
        properties = properties.filter(zip_code__icontains=zip_code)
    if city:
        properties = properties.filter(city__icontains=city)
    if address:
        properties = properties.filter(address__icontains=address)
    if min_price:
        properties = properties.filter(price__gte=min_price)
    if max_price:
        properties = properties.filter(price__lte=max_price)
    
    return render(request, 'product_list.html', {'properties': properties})

@login_required
def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    client_inquiries = Inquiry.objects.filter(property=property, client=request.user)
    invoices = Invoice.objects.filter(payment__property=property, payment__client=request.user)
    inquiries = Inquiry.objects.filter(property=property)
    is_favorite = request.user.is_authenticated and Favorite.objects.filter(property=property, user=request.user).exists()
    
    return render(request, 'product_detail.html', {
        'property': property,
        'client_inquiries': client_inquiries,
        'invoices': invoices,
        'is_favorite': is_favorite,
        'inquiries': inquiries
    })


@login_required
@user_passes_test(is_client)
def make_enquiry(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    
    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            inquiry = form.save(commit=False)
            inquiry.client = request.user  # The client making the enquiry
            inquiry.property = property  # The property being enquired about
            inquiry.save()
            messages.success(request, 'Your enquiry has been sent successfully.')
            return redirect('property_detail', property_id=property.id)
    else:
        form = InquiryForm()

    return render(request, 'inquiries/make_enquiry.html', {'form': form, 'property': property})



@login_required
@user_passes_test(is_client)
def toggle_favorite(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    favorite, created = Favorite.objects.get_or_create(property=property, user=request.user)

    if created:
        messages.success(request, 'Property has been added to your favorites.')
    else:
        favorite.delete()
        messages.success(request, 'Property removed from your favorites.')

    return redirect('property_detail', property_id=property.id)

@login_required
@user_passes_test(is_client)
def favorite_properties(request):
    favorites = request.user.favorite_properties.all()
    return render(request, 'inquiries/favorite_properties.html', {'favorites': favorites})

@login_required
@user_passes_test(is_client)
def remove_favorite(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    favorite = Favorite.objects.filter(property=property, user=request.user).first()

    if favorite:
        favorite.delete()
        messages.success(request, 'Property removed from your favorites.')
    else:
        messages.error(request, 'This property was not in your favorites.')

    return redirect('property_list')


@login_required
@user_passes_test(is_agent)
def client_details(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    interactions = ClientInteraction.objects.filter(client=client)
    
    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.client = client
            interaction.save()
            return redirect('client_details', client_id=client.id)
    else:
        form = InteractionForm()

    return render(request, 'inquiries/client_details.html', {
        'client': client,
        'interactions': interactions,
        'form': form,
    })

@login_required
@user_passes_test(is_agent)
def track_interaction(request, client_id):
    client = get_object_or_404(Client, id=client_id)

    if request.method == 'POST':
        form = InteractionForm(request.POST)
        if form.is_valid():
            interaction = form.save(commit=False)
            interaction.client = client
            interaction.save()
            return redirect('client_interactions', client_id=client.id)
    else:
        form = InteractionForm()

    return render(request, 'inquiries/track_interaction.html', {'form': form, 'client': client})

@login_required
@user_passes_test(is_agent)
def client_interactions(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    interactions = ClientInteraction.objects.filter(client=client)
    return render(request, 'inquiries/client_interactions.html', {'client': client, 'interactions': interactions})

def home(request):
    clients = Client.objects.all()
    return render(request, 'home.html', {'clients': clients})

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
