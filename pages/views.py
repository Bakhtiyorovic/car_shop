from django.shortcuts import render
from .models import *
# Create your views here.
def Home(request):
    home_entry = Home_page.objects.all()
    return render(request, 'index.html', {'home_entry': home_entry})

def Contact(request):
    return render(request, 'contact.html')

def Service(request):
    return render(request, 'service.html')

def Featured_Cars(request):
    return render(request, 'featured_cars.html')

def New_Cars(request):
    return render(request, 'new_cars.html')
