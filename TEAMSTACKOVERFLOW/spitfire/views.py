from django.shortcuts import render

# Create your views here.
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist


def index(request):
	"""
	put stuff here!
	"""

	# artistName = Artist.objects.all().get(first_name = 'Flo') #TODO Fix this
	# trackName = Track.objects.title()	

	return render(
		request,
		'index.html',
		context = {'artistName': "Artist Name", 'trackName': "Track Name", 'trackDescription': "Description of the track of artist, etc etc", 'upvoteCount': "6969", 'lyricsUserName': "Lyricist Username", 'lyrics': "I'm a spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical <br></br> individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual", },
	)

def profile(request):
	"""
	put stuff here!
	"""
	artistPic = Artist.objects.all().get(first_name = 'Flo').propic #this line doesnt work
	userName = Artist.objects.all().get(first_name = 'Flo')
	return render(
		request, 
		'profile.html',
		context = {'userName': userName, 'artistPic': artistPic},
	)

def track(request):

	"""
	put stuff here
	"""

	return render(
		request,
		'soundtrack.html',
		context = {},


	)

def artist(request):

	"""
	put stuff here
	"""

	return render(
		request,
		'profile.html',
		context = {},
	)


def genre(request):
	"""
	put stuff here
	"""

	return render(
		request,
		'profile.html',
		context = {},

	)


def lyrics(request):
	"""
	put stuff here
	"""

	return render(
	request,
	'profile.html',
	context = {},
	)




