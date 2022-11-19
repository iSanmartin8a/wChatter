from django.http import HttpResponse
from django.shortcuts import render
from chatter_web.models import Theme
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request, 'index.html')

def game(request):
    return render(request, 'game.html')

class Game(ListView):
    model = Theme
    paginate_by = 1