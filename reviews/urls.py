from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.search_game, name='search'),
    url(r'^listgame/', views.list_game, name='list'),
]