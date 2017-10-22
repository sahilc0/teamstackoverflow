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

	artistName = Artist.objects.all().get(first_name = 'Flo')
	numOfFollowers = Artist.objects.get(number_of_followers = 100).number_of_followers
	followingNumber = Artist.objects.get(first_name = 'Flo').number_following
	homeAddress = Artist.objects.get(first_name = 'Flo').homeAddress
	numOfSpits = Artist.objects.get(first_name = 'Flo').spits
	return render(
		request, 
		'profile.html',
		context = {'artistName': artistName, 
				   'artistPic': artistPic, 
				   'numOfFollowers': numOfFollowers, 
				   'followingNum': followingNumber, 
				   'userAddress': homeAddress,
				   'numOfSpits': numOfSpits},
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




