from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^soundtrack$', views.track, name='track'),
	url(r'^Artist$', views.artist, name='artist'),
	url(r'^genre$', views.genre, name='genre'),
	url(r'^lyrics$', views.lyrics, name='lyrics'),


]