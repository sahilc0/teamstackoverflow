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
		context = {'artistName': "Artist Name", 
				   'trackName': "Track Name", 
				   'trackDescription': "Description of the track of artist, etc etc", 
				   'upvoteCount': "6969", 
				   'lyricsUserName': "Lyricist Username", 
				   'lyrics': "I'm a spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical <br></br> individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual", 
				   },
	)

def profile(request):
	artistName = Artist.objects.all().get(first_name = 'Bob')
	numOfFollowers = Artist.objects.get(number_of_followers = 100).number_of_followers
	followingNumber = Artist.objects.get(first_name = 'Bob').number_following
	homeAddress = Artist.objects.get(first_name = 'Bob').homeAddress
	numOfSpits = Artist.objects.get(first_name = 'Bob').spits
	trackName = Track.objects.get(title = '10miles').title
	eminemTrackLyrics = Lyrics.objects.get(title = 'EminemTrack').text
	eminemRemixLyrics = Lyrics.objects.get(title = 'EminemRemix').text
	deadBeefLyrics = Lyrics.objects.get(title = 'DeadBeef').text
	artistOfLyric = Lyrics.objects.get(title = 'EminemTrack').artist
	lyricist1 = Lyrics.objects.get(title = 'EminemRemix').artist
	lyricist2 = Lyrics.objects.get(title = 'DeadBeef').artist
	trackName1 = Track.objects.get(title = '99Problems')
	trackName2 = Track.objects.get(title = 'UptownFunk')
	profileImage = Artist.objects.get(first_name = 'Bob').image
	return render(
		request, 
		'profile.html',
		context = {'artistName': artistName, 
				   'numOfFollowers': numOfFollowers, 
				   'followingNum': followingNumber, 
				   'userAddress': homeAddress,
				   'numOfSpits': numOfSpits,
				   'trackName': trackName,
				   'eminemTrackLyrics': eminemTrackLyrics,
				   'eminemRemixLyrics': eminemRemixLyrics,
				   'deadBeefLyrics': deadBeefLyrics,
				   'artistOfLyric': artistOfLyric,
				   'trackName1': trackName1,
				   'trackName2': trackName2,
				   'lyricist1': lyricist1,
				   'lyricist2': lyricist2,
				   'profileImage': profileImage},
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

def upload(request):
	"""
	put stuff here
	"""

	return render(
		request,
		'upload.html',
		context = {},
	)

def contest(request):
	"""
	put stuff here
	"""

	return render(
		request,
		'contest.html',
		context= {},
		)




