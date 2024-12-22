from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contacts.html')

