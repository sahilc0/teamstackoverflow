from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.contrib.auth.models import User
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Sponsor
from .forms import UserForm
from .forms import TrackForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse #this line might not be needed
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def create_profile(request):
	if request.method == 'POST':
		user_form = UserForm(request.POST)
		if user_form.is_valid():
			first_name = user_form.cleaned_data['first_name']
			last_name = user_form.cleaned_data['last_name']
			username = user_form.cleaned_data['username']
			password = user_form.cleaned_data['password']
			email = user_form.cleaned_data['email']
			city = user_form.cleaned_data['city']
			user = User.objects.create_user(username, email, password)
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			#we can substitute the bottom code with a @receiver decorator
			artist = Artist(user=user, firstName = user.first_name, lastName=user.last_name, city=city)
			artist.save()
			return render(request,'index.html')
	else:
		user_form = UserForm()
	return render(
		request,
		'create_profile.html',
		context = {
			'user_form':user_form,
		},
	)

def upvoteTrack(request, pk):
	track = get_object_or_404(Track, pk = pk)
	track.upvotes = track.upvotes + 1
	track.save()
	return HttpResponse(track.upvotes)

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
	#change the code above to dynamic

	topList = Track.objects.order_by('upvotes')[:3]
	topTrack1 = topList[0]



	track1Artist_Id = featTrack1.artist.id
	track2Artist_Id = featTrack2.artist.id
	track3Artist_Id = featTrack3.artist.id

	return render(
		request,
		'index.html',
		context = {'featTrack1': featTrack1,
				  'track1Artist_Id': track1Artist_Id,
  				  'track2Artist_Id': track2Artist_Id,
				  'track3Artist_Id': track3Artist_Id,
				  'topList': topList,
				  'topTrack1': topTrack1,


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
@login_required
def upload(request):
	if request.method == 'POST':
		user = request.user
		form = TrackForm(request.POST, request.FILES)
		if form.is_valid():
			title = form.cleaned_data['title']
			artist = form.cleaned_data['artist']
			#upvotes = form.cleaned_data['upvotes']
			genre = form.cleaned_data['genre']
			description = form.cleaned_data['description']
			keywords = form.cleaned_data['keywords']
			file = form.cleaned_data['mp3']
			track = Track(title=title, artist=artist, genre=genre, description=description, keywords=keywords, mp3=file)
			track.save()
			return HttpResponseRedirect(reverse('profile'))
	else:
		form = TrackForm()
	return render(request, 'trackForm.html', {'form': form})

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

#need to fix profile viewfunction, this is hardcoded. Implementation is not done yet, but its on the right track I think.
@login_required
def profile(request):
	user = request.user
	artist = user.artist
	tracks = Track.objects.filter(artist = artist).order_by('-upvotes')
	return render(
		request,
		'profile.html',
		context = { 'artist': artist,
					'tracks': tracks,
				  },
	)

#ronny's testing stuff out below this


@login_required
def getTrackInfo(request, pk):
	track = get_object_or_404(Track, pk = pk)
	if request.method == 'GET':
		return render(request, 'soundtrack.html', {'track': track})

@login_required
def getArtistInfo(request, pk):
	artist = get_object_or_404(Artist, pk = pk)
	if request.method == 'GET':
		return render(request, 'profile.html', {'artist': artist})
