from django.conf.urls import url
from . import views

from django.conf.urls.static import static
from django.conf import settings
#testing the last 2 lines above

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^soundtrack/lyrics/(?P<pk>[-\w]+)$', views.getLyricsInfo, name='lyrics'),
    url(r'^contest$', views.contest, name='contest'),
    url(r'^create_contest$', views.create_contest, name='create_contest'),
    url(r'^create_profile$', views.create_profile, name='create_profile'),
    url(r'^edit_profile$',views.edit_profile,name='edit_profile'),
    url(r'^soundtrack/(?P<pk>[-\w]+)$', views.getTrackInfo, name='trackInfo'),
    url(r'^soundtrack/(?P<pk>[-\w]+)/upvote$', views.upvoteTrack, name='upvote_track'),
    url(r'^lyric/(?P<pk>[-\w]+)/upvote$', views.upvoteLyric, name='upvote_lyric'),
    url(r'^soundtrack/(?P<pk>[-\w]+)/lyric_comment$',views.getTrackInfo,name='lyric_comment'),
    url(r'^soundtrack/(?P<pk>[-\w]+)/track_comment$',views.getTrackInfo,name='track_comment'),
    url(r'^profile/upload$', views.upload, name='upload'),
    url(r'^profile/(?P<pk>[-\w]+)$', views.getArtistInfo, name='artistInfo'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/(?P<pk>[-\w]+)/follow$', views.addFollower, name='add_follower'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
