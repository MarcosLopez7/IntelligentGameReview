from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def search_game(request):
    return render(request, 'reviews/search.html')


def list_game(request):
    texto = request.GET['texto']
    games = Nombre.objects.filter(nombre__icontains=texto)
    reviews = []

    for game in games:
        reviews.append(General.objects.get(nombre = game))

    return render(request, 'reviews/results.html', {'reviews': reviews})

@register.tag
def game(request, pk):
    game = get_object_or_404(General, pk = pk)
    return render(request, 'reviews/game.html', {'game': game})
    
