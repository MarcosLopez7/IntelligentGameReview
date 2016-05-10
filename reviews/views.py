from django.shortcuts import render
from .models import *
from .proyectoLDAW import *

# Create your views here.
def search_game(request):
    return render(request, 'reviews/search.html')


def list_game(request):
    texto = request.GET['texto']
    games = Nombre.objects.filter(nombre__icontains=texto)
    reviews = []
    fotos = []
    i = 0
    for game in games:
        reviews.append(General.objects.filter(nombre = game))
        fotos.append(reviews[i].foto[7:])
        i = i + 1

    return render(request, 'reviews/results.html', {'reviews': reviews, 'fotos': fotos})

def game(request, pk):
    game = General.objects.get(pk = pk)
    
