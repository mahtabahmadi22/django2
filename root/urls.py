from django.urls import path 
from .views import *

app_name = 'root'
urlpatterns = [
    path('',home),
    path('about',about),
    path('contact',contact)
]

