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

# Create your views here.
def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

class Game(ListView):
    model = Theme
    paginate_by = 1

    def get_queryset(self):
        queryset = Theme.objects.all().distinct().order_by('?')
        return queryset

class Categories(ListView):
    model = Genre

class SearchResultsListView(ListView):
    model = Theme
    paginate_by = 1
    template_name = 'chatter_web/search_themes.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            query_splitted = query.split(", ")[:-1]
            print(query_splitted)
            self.query = query
            queryset = Theme.objects.none()
            for word in query_splitted:
                id_generos = Genre.objects.filter(name__icontains=word).values_list('id', flat=True)
                print(id_generos)
                object_list = Theme.objects.filter(genre__in=id_generos).values_list('theme', flat=True)
                print(object_list)
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

def searchThemes(request, self):
    query = self.request.GET.get('q')


    if query is not None:
        query_splitted = query.split(", ")[:-1]
        print(query_splitted)
        self.query = query
        queryset = Theme.objects.none()
        for word in query_splitted:
            id_generos = Genre.objects.filter(name__icontains=word).values_list('id', flat=True)
            print(id_generos)
            object_list = Theme.objects.filter(genre__in=id_generos).values_list('theme', flat=True)
            print(object_list)
            queryset |= object_list

        p = Paginator(queryset, 1)
        page = p.page(2)
        context = {'themes': page}

        return render(request, 'chatter_web/search_themes.html', context)
    else:
        return []