from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings
#testing the last 2 lines above

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^soundtrack$', views.track, name='track'),
	url(r'^lyrics$', views.lyrics, name='lyrics'),
	url(r'^profile$', views.profile, name='profile'),
	#url(r'^upload$', views.upload, name='upload'), #this can be used as include(), but let this be for now.
	url(r'^contest$', views.contest, name='contest'),
    url(r'^create_profile$', views.create_profile, name='create_profile'),
    #url(r'^profile/track$', views.makeTrack, name='makeTrack'),
    url(r'^soundtrack/(?P<pk>[-\w]+)$', views.getTrackInfo, name='trackInfo'),
	url(r'^soundtrack/(?P<pk>[-\w]+)/upvote$', views.upvoteTrack, name='upvote_track'),
	url(r'^lyric/(?P<pk>[-\w]+)/upvote$', views.upvoteLyric, name='upvote_lyric'),
    url(r'^profile/upload$', views.upload, name='upload'),
    url(r'^profile/(?P<pk>[-\w]+)$', views.getArtistInfo, name='artistInfo'),
	url(r'^soundtrack/create_comment$', views.create_comment, name='create_comment'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
