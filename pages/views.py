from django.shortcuts import render

# Create your views here.
def Home(request):
    return render(request, 'index.html')

# def Brands(request):
#     return render(request, 'brands.html')

# def Contact(request):
#     return render(request, 'contact.html')

# def Service(request):
#     return render(request, 'service.html')

# def Featured_Cars(request):
#     return render(request, 'featured_cars.html')

# def New_Cars(request):
#     return render(request, 'new_cars.html')
