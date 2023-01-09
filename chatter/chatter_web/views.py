from urllib import request, response
from django.http import HttpResponse
from django.shortcuts import render
from chatter_web.models import Theme, Genre
from django.views.generic import ListView
import datetime
from django.core.cache import cache
import urllib.request
import pickle
from django.core import serializers
import json
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.core.cache import cache

# Create your views here.
def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

class Game(ListView):
    model = Theme
    paginate_by = 1

    def get_queryset(self):
        queryset_list = Theme.objects.all().order_by('?')
        queryset_list = cache.get('queryset_list')
        if not queryset_list:
            queryset_list = Theme.objects.all().order_by('?')
            cache.set('queryset_list',queryset_list)
        return queryset_list


class Categories(ListView):
    model = Genre

class SearchResultsListView(ListView):
    model = Theme
    paginate_by = 1
    template_name = 'chatter_web/search_themes.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            query_splitted = query.split(",")
            self.query = query
            queryset = Theme.objects.none()
            for word in query_splitted:
                id_generos = Genre.objects.filter(short__icontains=word).values_list('id', flat=True)
                object_list = Theme.objects.filter(genre__in=id_generos).distinct().values_list('theme', flat=True).order_by('?')
                queryset |= object_list
            return queryset
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['busqueda'] = self.queryset
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        context['q'] = self.request.GET.get('q')
        return context