from django.shortcuts import render

# Create your views here.
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist


def index(request):
	trackDescription1 = Track.objects.get(title='Rolling in the Deep').description
	trackDescription2 = Track.objects.get(title='UptownFunk').description
	trackDescription3 = Track.objects.get(title='99Problems').description
	featArtist1 = Track.objects.get(title='Rolling in the Deep').artist
	featArtist2 = Track.objects.get(title='Let It Go!').artist
	featArtist3 = Track.objects.get(title='99Problems').artist
	featTrackName1 = Track.objects.get(id = '5443d08db1ba486a81cf27b2dcf71158')
	featTrackName3 = Track.objects.get(id = 'b95a3265471b43f49172029cfdceaeb1')
	featTrackName2 = Track.objects.get(id = '0f8779be3ad340acbf192bbe48a6d1a8')
	lyricsUserName1 = Lyrics.objects.get(artist_id = '4d4422f7743944e98239940cf6f27963').artist
	lyricsUserName2 = Lyrics.objects.get(artist_id = '986a07ef4b824899b1c09983a373fa63').artist
	lyrics1 = Lyrics.objects.get(id = 'a61f37d97ecd4b84a009ef48c41b457f').text
	lyrics2 = Lyrics.objects.get(id = '25863132de194e3c8d1b3b6c49a91f90').text
	topArtistName1 = Artist.objects.get(first_name = 'Chance the').first_name + " " + Artist.objects.get(first_name = 'Chance the').last_name
	topArtistName2 = Artist.objects.get(id = '4c8b7e638ce24032ac6eb8225eafa76a').first_name
	topArtistName3 = Artist.objects.get(id = '2e0a396d94cb446198a89d1bd921ee58').first_name
	topTrackName1 = Track.objects.get(artist_id = '993722bac92d4cd087497fbf24580bbb')
	topTrackName2 = Track.objects.get(artist_id = '4c8b7e638ce24032ac6eb8225eafa76a').title
	topTrackName3 = Track.objects.get(artist_id = '2e0a396d94cb446198a89d1bd921ee58').title
	yesterdayArtist = Artist.objects.get(id = '72f7f315034b4d9fbd7f140b8270156f').first_name
	yesterdayTrack = Track.objects.filter(artist_id = '72f7f315034b4d9fbd7f140b8270156f')[1].title
	return render(
		request,
		'index.html',
		context = {'trackDescription1': trackDescription1, 
   				   'trackDescription2': trackDescription2, 
				   'trackDescription3': trackDescription3, 
				   'featArtist1': featArtist1,
				   'featArtist2': featArtist2,
				   'featArtist3': featArtist3,
				   'featTrackName1': featTrackName1,
				   'featTrackName3': featTrackName3,
				   'featTrackName2': featTrackName2,
				   'lyrics1': lyrics1,
				   'lyrics2': lyrics2,
				   'topArtistName1': topArtistName1,
   				   'topArtistName2': topArtistName2,
				   'topArtistName3': topArtistName3,
				   'topTrackName1': topTrackName1,
				   'topTrackName2': topTrackName2,
				   'topTrackName3': topTrackName3,
				   'yesterdayArtist': yesterdayArtist,
				   'yesterdayTrack': yesterdayTrack,
				   'upvoteCount': "6969", 
				   'lyricsUserName2': lyricsUserName2,
				   'lyricsUserName1': lyricsUserName1, 
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




