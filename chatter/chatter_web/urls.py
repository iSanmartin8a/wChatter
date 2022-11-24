# Creamos urls.py en la carpeta catalog
from django import views
from django.urls import path
from .views import index, Game, Categories, SearchResultsListView

urlpatterns = [
    path('', index, name='index'),
    path('game/', Game.as_view(), name='game'),
    path('categories/', Categories.as_view(), name='categories'),
    path('busqueda/', SearchResultsListView.as_view(), name='buscar'),
]

