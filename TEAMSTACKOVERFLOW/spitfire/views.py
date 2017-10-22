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
	artistName = Artist.objects.all().get(first_name = 'Flo')
	#numOfFollowers = Artist.get(number_of_followers)
	return render(
		request, 
		'profile.html',
		context = {'artistName': artistName, 'artistPic': artistPic},
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
#change request page for the functions below~~~~~~~~~~~~~~~~~~~~~~~~~~

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




