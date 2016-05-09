from django.shortcuts import render
from .models import *

# Create your views here.
def search_game(request):
    return render(request, 'reviews/search.html')


def list_game(request):
    texto = request.GET['texto']
    games = Nombre.objects.filter(nombre__icontains=texto)
    reviews = []
    for game in games:
        reviews.append(General.objects.filter(nombre = game))

    return render(request, 'reviews/results.html', {'reviews': reviews})

