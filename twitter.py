import tweepy #docs http://tweepy.readthedocs.org/en/v3.5.0/
from vaderSentiment.vaderSentiment import sentiment as vaderSentiment 
import datetime
from sklearn import tree
#from django.core.management import setup_environ
#from IGR import settings
import os, sys
import numpy as np

proj_path = "/home/tuffk/IGR"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IGR.settings")
sys.path.append(proj_path)

os.chdir(proj_path)

from django.core.wsgi import get_wsgi_application
application= get_wsgi_application()

from reviews.models import *

CONSUMER_KEY = 'Q3qAKPCSRKv7mZkp1uImUTtY9'
CONSUMER_SECRET = 'tTV3S6YX5HlJjcMbKvtJ7TugR87rq4CxPKzLuBsQ9d9srUPi6o'
ACCESS_TOKEN = '4854893381-Bt0IBTAckLWInaVuXJwkgMbEF3vahNPi2RlFVGe'
ACCESS_TOKEN_SECRET = 'kUP7reEgASw7gXwWJ2cGQKmHmu1QwiZaZkQmBscww9au5'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#id del ultimo tweet que se analizo
#ultimo_tweet = 0


#conector = conn.DBConnector()
#conector.load()
#conector.connect()

#Asociacion con hashtags
dicc = {'Halo 3' : '#Halo3', 'Halo 3: ODST' : '#Halo3', 'Halo 2' : '#Halo2', 'Age of Empires III' : '#AgeOfEmpires',  'Age of Empire 2 HD' : '#AgeOfEmpires', 'League of Legends' : '#LeagueOfLegends', 'Dark Souls 3' : '#DarkSouls3', 'Bloons TD 5' : '#BloonsTD', 'Final Fantasy XIV: Heavensward' : '#FFXIV', 'Grand Theft Auto V' : '#GTAV', 'Castlevania: Lords of Shadow' : '#Castlevania', 'The Elder Scrolls V: Skyrim' : '#Skyrim', 'Gears of War' : '#GearsOfWar', 'Guild Wars 2' : '#GW2', 'Infamous' : '#Infamous', 'Call of Duty: Black Ops' : '#BlackOps', 'Conker: Live and Reloaded' : '#Conker', 'Dragonball: Xenoverse' : '#Xenoverse', 'Prince of Persia: The Forgotten Sands' : '#PrinceOfPersia', 'Star Wars: Battlefront' : '#Battlefront'}

games = General.objects.all()


#Arbol de Decision
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


                  #buscar calificacion del dia de hoy

#buscar tweets desde esta fecha
date = datetime.datetime.now() - datetime.timedelta(days=1)


muypositivo = 0
positivo = 0
neutral = 0
negativo = 0
muynegativo = 0
categoria = 0

dateFrom = date.strftime('%Y-%m-%d')

#buscar tweets hasta esta fecha
date = date + datetime.timedelta(days=1)
dateTo = date.strftime('%Y-%m-%d')

for game in games:
    idActualizar = game.pk
    if dicc[game.nombre.nombre]:
        hashtag = dicc[game.nombre.nombre]
    else:
        print ('no se encontro hashtag\n')
        break
    results = api.search(q=hashtag, count=100, result_type="recent", lang="en", exclude="retweets", since=dateFrom, until=dateTo)
    actualizar = True      
    for tweet in results:           
        vs = vaderSentiment(tweet.text.encode('ascii', 'ignore'))
        v=list(vs.values())
        #saca la polaridad de -1 a 1
        polaridad = v[3]        
        #print "POLARIDAD:" + str(polaridad) + "\n\n"
        if 1.0 >= polaridad > 0.5:
            muypositivo+=1
        if 0.5 >= polaridad > 0:
            positivo+=1
        if polaridad == 0:
            neutral+=1
        if 0 > polaridad > -0.5:
            negativo+=1
        if -0.5 >= polaridad >= -1.0:
            muynegativo+=1          
    if len(results) < 3:
        actualizar = False  
    else:
        actualizar = True
        #print "muy negativo: " + str(muynegativo) + "\nnegativo: " + str(negativo) + "\nneutral: " + str(neutral) + "\npositivo: " + str(positivo) + "\nmuypositivo: " + str(muypositivo) + "\n\nTOTAL: " + str(muynegativo+negativo+neutral+positivo+muypositivo)
        promedio = (muypositivo + positivo*.75 + neutral*.5 + negativo*.25)/(muynegativo+negativo+neutral+positivo+muypositivo)
        promedio = (promedio * 100)/80
        if promedio < 0.2:
            categoria = 1
        if 0.2 <= promedio < 0.4:
            categoria = 2
        if 0.4 <= promedio < 0.6:
            categoria = 3
        if 0.6 <= promedio < 0.8:
            categoria = 4
        if promedio >= 0.8:
            categoria = 5
    if actualizar:
        
        
        updateGame = General.objects.filter(pk = idActualizar).first()
        
        #rodando..
        
        updateGame.calificacion1=updateGame.calificacion2
        updateGame.calificacion2=updateGame.calificacion3
        updateGame.calificacion3=updateGame.calificacion4
        updateGame.calificacion4=updateGame.calificacion5                                
        updateGame.calificacion5 = categoria
        updateGame.save()
        
        #las variables necesarias para la prediccion
        variables_para_pred=[]
        variables_para_pred.append(game.plataforma.pk)
        variables_para_pred.append(game.player.pk)
        variables_para_pred.append(game.esrb.pk)
        variables_para_pred.append(game.publisher.pk)
        variables_para_pred.append(game.serie.pk)
        variables_para_pred.append(game.calificacion1)
        variables_para_pred.append(game.calificacion2)
        variables_para_pred.append(game.calificacion3)
        variables_para_pred.append(game.calificacion4)
        variables_para_pred.append(game.calificacion5)
        

        predArray = np.reshape(variables_para_pred, (1,-1))
        #regresa una calificacion predicha de manana
        prediccion = modelo.predict(predArray)[0]
            
        #actualizar el score de manana
        updateGame.calificacionP = prediccion
        updateGame.save()
        
    else:
        print ('no hay suficientes tweets')


