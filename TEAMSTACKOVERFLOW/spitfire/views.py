from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User

from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Sponsor

def create_profile(request):

	if request.method == 'POST':
		user_form = UserForm(request.POST, instance = request.user)
		artist_form = ArtistForm(request.POST, instance=request.user.artist)
		if user_form.is_valid() and artist_form.is_valid():
			user_form.save()
			artist_form.save()
			return redirect('profile')
		else:
			messages.error(request, _('Please correct the error below.'))
	else:
		user_form = UserForm(instance=request.user)
		artist_form = ArtistForm(request.POST, instance=request.user.artist)

	return render
	(
		request,
		'create_profile.html',
		context = 
		{
			'user_form':user_form,
			'artist_form':artist_form,
		}
	)

def index(request):

	featTrack1 = Track.objects.get(title='Rolling in the Deep')
	featTrack2 = Track.objects.get(title='UptownFunk')
	featTrack3 = Track.objects.get(title='99Problems')
	topTrack = Track.objects.get(title = 'Rolling in the Deep')
	topTrack2 = Track.objects.get(title = 'UptownFunk')
	topTrack3 = Track.objects.get(title = '10miles')
	lyricsList1 = Lyrics.objects.filter(Track = '5443d08db1ba486a81cf27b2dcf71158')
	lyricsList2 = Lyrics.objects.filter(Track = '445e3187e4b4468bb6c983d2b13244e7')
	lyricsList3 = Lyrics.objects.filter(Track = 'e4dd123404ed43618195ebe356eaddd7')
	yesterdayTrack = Track.objects.get(id = 'b95a3265471b43f49172029cfdceaeb1')
	yesterdayLyrics = Lyrics.objects.filter(Track = yesterdayTrack.id)

	return render(
		request,
		'index.html',
		context = {'featTrack1': featTrack1, 
						 'featTrack2': featTrack2, 
					 'featTrack3': featTrack3, 
					 'lyricsList1': lyricsList1[0],
					 'lyricsList12': lyricsList1[1],
					 'lyricsList2': lyricsList2[0],
					 'lyricsList21': lyricsList2[1],
					 'lyricsList3': lyricsList3[0],
					 'lyricsList31': lyricsList3[1],
					 'topTrack': topTrack,
					 'topTrack2': topTrack2,
					 'topTrack3': topTrack3,
					 'yesterdayTrack': yesterdayTrack,
					 'yesterdayLyric1': yesterdayLyrics[0],
					 'yesterdayLyric2': yesterdayLyrics[1],
					 'upvoteCount': "6969", 
								 'audio1': "track_default.mp3",
								 'audio2': "track_default.mp3",
								 'audio3': "track_default.mp3",
								 'yesterdayAudio': "track_default.mp3",
					 'lyrics': "I'm a spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical <br></br> individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual spiritual lyrical spiritual lyrical individual", 
					 },
	)

def profile(request):
	artist = Artist.objects.get(id = '72f7f315034b4d9fbd7f140b8270156f')
	tracks = Track.objects.filter(artist = '72f7f315034b4d9fbd7f140b8270156f').order_by('-upvotes')

	return render(
		request,
		'profile.html',
		context = { 'artist': artist,
								'tracks': tracks,
								},
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

	sponsor1 = Sponsor.objects.get (name = 'Red Bull')
	sponsor2 = Sponsor.objects.get (name = 'Google')
	sponsor3 = Sponsor.objects.get (name = 'Coca-Cola')

	return render(
		request,
		'contest.html',
		context= {'sponsor1':sponsor1, 'sponsor2':sponsor2, 'sponsor3':sponsor3, }
		)
