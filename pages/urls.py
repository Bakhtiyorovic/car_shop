from django.urls import path
from .views import *

urlpatterns = [
    path('', Home, name='home'),
    path('contact/', Contact, name='contact'),
    path('featured_cars/', Featured_Cars, name='feature_cars'),
    path('new_cars/', New_Cars, name='new_cars'),
    path('service/', Service, name='service'),
]

