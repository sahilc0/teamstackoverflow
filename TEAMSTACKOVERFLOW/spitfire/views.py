from django.shortcuts import render

# Create your views here.
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Sponsor


def index(request):

	featTrack1 = Track.objects.get(title='Rolling in the Deep')
	featTrack2 = Track.objects.get(title='UptownFunk')
	featTrack3 = Track.objects.get(title='99Problems')


	lyrics1 = Lyrics.objects.get(Track = '5443d08db1ba486a81cf27b2dcf71158')
	lyrics2 = Lyrics.objects.get(Track = '445e3187e4b4468bb6c983d2b13244e7')


	topTrack = Track.objects.get(title = 'Rolling in the Deep')
	topTrack2 = Track.objects.get(title = 'UptownFunk')
	topTrack3 = Track.objects.get(title = '10miles')



	#topTrackName1 = Track.objects.get(artist = topArtistObject1).title
	#topTrackName2 = Track.objects.get(artist = topArtistObject2).title
	#topTrackName3 = Track.objects.get(artist = topArtistObject3).title
	
	yesterdayArtist = Artist.objects.get(id = '72f7f315034b4d9fbd7f140b8270156f').first_name
	yesterdayTrack = Track.objects.filter(artist_id = '72f7f315034b4d9fbd7f140b8270156f')[1].title
	return render(
		request,
		'index.html',
		context = {'featTrack1': featTrack1, 
   				   'featTrack2': featTrack2, 
				   'featTrack3': featTrack3, 

				   'lyrics1': lyrics1,
				   'lyrics2': lyrics2,
				   
				   'topTrack': topTrack,
				   'topTrack2': topTrack2,
				   'topTrack3': topTrack3,






	
				   'yesterdayArtist': yesterdayArtist,
				   'yesterdayTrack': yesterdayTrack,
				   'upvoteCount': "6969", 
				   #'lyricsUserName2': lyricsUserName2,
				   #'lyricsUserName1': lyricsUserName1, 
           'audio1': "track_default.mp3",
           'audio2': "track_default.mp3",
           'audio3': "track_default.mp3",
           'yesterdayAudio': "track_default.mp3",
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
           'audio1': "track_default.mp3",
           'audio2': "track_default.mp3",
           'audio3': "track_default.mp3",
				   'profileImage': profileImage},
	)

def track(request):
	
	thisArtist = Artist.objects.get(id = '4c8b7e638ce24032ac6eb8225eafa76a')
	thisTrack = Track.objects.get(artist_id = thisArtist.id)
	
	lyric1 = Lyrics.objects.get(id = 'd40bd2d5970a4760b7a7ea56e7628759')

	comment1 = LyricComment.objects.get(id = 'ec4862f401974ba4ba592ff9c0be1794')

	lyric2 = Lyrics.objects.get(id = 'd40bd2d5970a4760b7a7ea56e7628759')

	comment2 = LyricComment.objects.get(id = 'ec4862f401974ba4ba592ff9c0be1794')
	
	
	return render(
		request,
		'soundtrack.html',
		context = {'thisTrack': thisTrack,
				   'thisArtist': thisArtist,
				   'lyric1': lyric1,
				   'comment1': comment1,
   				   'lyric2': lyric2,
				   'comment2': comment2,
				  },


	)
#change request page for the functions below~~~~~~~~~~~~~~~~~~~~~~~~~~


def lyrics(request):
  track = Track.objects.get(title="Rudolph the Reindeer")

  return render(
  	request,
  	'lyrics-sync.html',
  	context = {
                'trackName': track.title,
                'artistName': track.artist,
                'audio1': "track_default.mp3",
                },
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
	sponsor_name1 = Sponsor.objects.get(sponsor_name='Red Bull').sponsor_name
	sponsor_name2 = Sponsor.objects.get(sponsor_name='Google').sponsor_name
	sponsor_name3 = Sponsor.objects.get(sponsor_name='Coca-Cola').sponsor_name

	sponsor_description1 = Sponsor.objects.get(sponsor_description='This contest is sponsored by Red Bull. Create a track based on the sound of Red Bull giving you wings. Winner will get a free trip to our HQ in LA and $10,000')
	sponsor_description2 = Sponsor.objects.get(sponsor_description='This contest is sponsored by Google. Create a track based on how the Google Assistant can help you in your everyday life. Winner gets $20,000 and a free trip to New York City.')
	sponsor_description3 = Sponsor.objects.get(sponsor_description='This contest is sponsored by Coke. Create a track based on the refreshing feeling that Coke gives you. Or something like that.')

	# sponsor_image1 = Sponsor.objects.get(sponsor_image='http://static.djbooth.net/pics-features/chance-3-artwork.jpg').sponsor_image
	# sponsor_image2 = Sponsor.objects.get(sponsor_image='http://static.djbooth.net/pics-features/chance-3-artwork.jpg').sponsor_image
	# sponsor_image3 = Sponsor.objects.get(sponsor_image='http://static.djbooth.net/pics-features/chance-3-artwork.jpg').sponsor_image

	
	return render(
		request,
		'contest.html',
		context= {'sponsor_name1': sponsor_name1, 'sponsor_name2': sponsor_name2, 'sponsor_description1': sponsor_description1, 'sponsor_description2': sponsor_description2, 'sponsor_name3': sponsor_name3, 'sponsor_description3': sponsor_description3},
		)




