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
    paginate_by = 1
    template_name = 'chatter_web/search_themes.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            query_splitted = query.split(", ")[:-1]
            print(query_splitted)
            if query:
                self.query = query
                queryset = Theme.objects.none()
                for word in query_splitted:
                    id_generos = Genre.objects.filter(name__icontains=word).values_list('id', flat=True)
                    print(id_generos)
                    object_list = Theme.objects.filter(genre__in=id_generos).values_list('theme', flat=True)
                    print(object_list)
                    queryset |= object_list
                print(queryset)
                return queryset
            else:
                return []
        else:
            return []

    def get_context_data(self, **kwargs):
        context = super(SearchResultsListView, self).get_context_data(**kwargs)
        context['busqueda'] = self.query
        context['anterior'] = self.request.META.get('HTTP_REFERER')
        return super().get_context_data(**kwargs)