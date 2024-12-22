
from django.urls import path

# from app.views import create_movie

from .views import *
from . import views

urlpatterns = [
 


    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contact, name='contacts'),

]


