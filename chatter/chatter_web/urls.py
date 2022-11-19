# Creamos urls.py en la carpeta catalog
from django import views
from django.urls import path
from .views import index, Game

urlpatterns = [
    path('', index, name='index'),
    path('game/', Game.as_view(), name='game'),
]

