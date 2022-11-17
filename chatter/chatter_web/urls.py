# Creamos urls.py en la carpeta catalog
from django import views
from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='index'),
]

