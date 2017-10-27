from django.shortcuts import render

# Create your views here.
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist


def index(request):
	#descriptions of featured Tracks
	trackDescription1 = Track.objects.get(title='Rolling in the Deep').description
	trackDescription2 = Track.objects.get(title='UptownFunk').description
	trackDescription3 = Track.objects.get(title='99Problems').description
	#artists in the featured section
	featArtist1 = Track.objects.get(description = trackDescription1).artist
	featArtist2 = Track.objects.get(description = trackDescription2).artist
	featArtist3 = Track.objects.get(description = trackDescription3).artist
	#track names of tracks in feature sections
	featTrackName1 = Track.objects.get(description = trackDescription1).title
	featTrackName2 = Track.objects.get(description = trackDescription2).title
	featTrackName3 = Track.objects.get(description = trackDescription3).title

	lyricsUserName1 = Lyrics.objects.get(artist_id = '4d4422f7743944e98239940cf6f27963').artist
	lyricsUserName2 = Lyrics.objects.get(artist_id = '986a07ef4b824899b1c09983a373fa63').artist
	lyrics1 = Lyrics.objects.get(artist = lyricsUserName1).text
	lyrics2 = Lyrics.objects.get(artist = lyricsUserName2).text
	
	topArtistObject1 = Artist.objects.get(id = '993722bac92d4cd087497fbf24580bbb')
	topArtistObject2 = Artist.objects.get(id = '4c8b7e638ce24032ac6eb8225eafa76a')
	topArtistObject3 = Artist.objects.get(id = '2e0a396d94cb446198a89d1bd921ee58')
	topArtistName1 = topArtistObject1.first_name + " " + topArtistObject1.last_name
	topArtistName2 = topArtistObject2.first_name
	topArtistName3 = topArtistObject3.first_name
	
	topTrackName1 = Track.objects.get(artist = topArtistObject1).title
	topTrackName2 = Track.objects.get(artist = topArtistObject2).title
	topTrackName3 = Track.objects.get(artist = topArtistObject3).title
	
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
	
	artistObject = Artist.objects.get(id = '4c8b7e638ce24032ac6eb8225eafa76a')
	TrackName =	Track.objects.get(artist_id = artistObject.id).title
	ArtistName = artistObject.first_name + " " + artistObject.last_name
	Keywords = Track.objects.get(title = TrackName).keywords
	
	lyricObject1 = Lyrics.objects.get(id = 'd40bd2d5970a4760b7a7ea56e7628759')
	lyricName1 = lyricObject1.title
	lyrics1 = lyricObject1.text

	commentObject = LyricComment.objects.get(id = 'ec4862f401974ba4ba592ff9c0be1794')
	commenter = commentObject.artist.first_name
	comment = commentObject.text

	lyricObject2 = Lyrics.objects.get(id = '25863132de194e3c8d1b3b6c49a91f90')
	lyricName2 = lyricObject2.title
	lyrics2 = lyricObject2.text

	commentObject2 = LyricComment.objects.get(id = 'e861350b34af4b28916f266b05e97b81')
	commenter2 = commentObject2.artist.first_name
	comment2 = commentObject.text
	
	
	return render(
		request,
		'soundtrack.html',
		context = {'TrackName': TrackName,
				   'ArtistName': ArtistName,
				   'Keywords': Keywords,
				   'lyricName1': lyricName1,
				   'lyrics1': lyrics1,
				   'commenter': commenter + " " + "says",
				   'comment': comment,
   				   'lyricName2': lyricName2,
				   'lyrics2': lyrics2,
				   'commenter2': commenter2 + " " + "says",
				   'comment2': comment2,
				  },


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




