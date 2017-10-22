from django.shortcuts import render

# Create your views here.
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist


def index(request):
	"""
	put stuff here!
	"""

	return render(
		request,
		'index.html',
		context = {},
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




