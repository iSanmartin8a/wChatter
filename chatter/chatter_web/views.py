from urllib import request
from django.http import HttpResponse
from django.shortcuts import render
from chatter_web.models import Theme, Genre
from django.views.generic import ListView
import datetime

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
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            self.query = query
            object_list = Theme.objects.filter(genre__icontains=query)
            return object_list
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['busqueda'] = self.query
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        return super().get_context_data(**kwargs)