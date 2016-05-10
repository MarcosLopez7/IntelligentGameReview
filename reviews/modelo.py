from .models import *

games = General.objects.all()
lista = []
for game in games:
    listaTemp = []
    listaTemp.append(game.plataforma.pk)
    listaTemp.append(game.player.pk)
    listaTemp.append(game.esrb.pk)
    listaTemp.append(game.publisher.pk)
    listaTemp.append(game.serie.pk)
    listaTemp.append(game.calificacion1)
    listaTemp.append(game.calificacion2)
    listaTemp.append(game.calificacion3)
    listaTemp.append(game.calificacion4)
    listaTemp.append(game.calificacion5)
    lista.append(listaTemp)

y = games.values_list('calificacionP')

modelo = tree.DecisionTreeClassifier()
modelo.fit(lista, y)
'''
for game in games:
    listaTemp2 = []
    listaTemp2.append(game.plataforma.pk)
    listaTemp2.append(game.player.pk)
    listaTemp2.append(game.esrb.pk)
    listaTemp2.append(game.publisher.pk)
    listaTemp2.append(game.serie.pk)
    listaTemp2.append(game.calificacion2)
    listaTemp2.append(game.calificacion3)
    listaTemp2.append(game.calificacion4)
    listaTemp2.append(game.calificacion5)
    listaTemp2.append(game.calificacionp)
    lista.append(listaTemp2)
x=listaTemp2
'''
results = modelo.predict(x)