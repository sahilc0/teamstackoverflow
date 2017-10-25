from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^soundtrack$', views.track, name='track'),
	url(r'^artist$', views.artist, name='artist'),
	url(r'^genre$', views.genre, name='genre'),
	url(r'^lyrics$', views.lyrics, name='lyrics'),
	url(r'^profile$', views.profile, name='profile'),
	url(r'^upload$', views.upload, name='upload'), #this can be used as include(), but let this be for now.
	url(r'^contest$', views.contest, name='contest'),
]
