from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.contrib.auth.models import User
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Sponsor
from .forms import UserForm
from .forms import TrackForm
from .forms import CommentForm
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
			img = user_form.cleaned_data['image']
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			#we can substitute the bottom code with a @receiver decorator
			artist = Artist(user=user, firstName = user.first_name, lastName=user.last_name, city=city, image=img)
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

def create_comment (request):
	if request.method == 'GET':
		thing = request.GET.get(user_comment, None) #tried post but wasn't working so GET
		print (thing)
		comment = CommentForm(request.POST)
		if comment.is_valid():
			comment = comment.cleaned_data['comment'];
			track_comment = TrackComment (upvotes=0, text=comment, track=track)
			track_comment.save()
		return render(request, 'soundtrack.html')
	else:
		comment = CommentForm()

	return render(
		request,
		'soundtrack.html',
		context = {
		'comment': comment
		},
	)

def search(request):
	search_field = request.GET.get('search_field', None)
	search_results = Track.objects.filter(title__contains=search_field) | Track.objects.filter(description__contains=search_field) | Track.objects.filter(keywords__contains=search_field)

	return render(request, "search_result.html", context = {'tracks': search_results,},)

@login_required
def upvoteTrack(request, pk):
	track = get_object_or_404(Track, pk = pk)

	if request.method == 'POST':
		track.upvotes = track.upvotes + 1
		track.save()
		return HttpResponse(track.upvotes)

@login_required
def upvoteLyric(request, pk):
	lyric = get_object_or_404(Lyrics, pk = pk)

	if request.method == 'POST':
		lyric.upvotes = lyric.upvotes + 1
		lyric.save()
		return HttpResponse(lyric.upvotes)

def index(request):
	featTrack1 = Track.objects.get(title='Rolling in the Deep')
	featTrack2 = Track.objects.get(title='Bye Bye Bye')
	featTrack3 = Track.objects.get(title='99Problems')
	yesterdayTrack = Track.objects.get(id = 'b95a3265471b43f49172029cfdceaeb1')
	yesterdayLyrics = Lyrics.objects.filter(Track = yesterdayTrack.id)
	#change the code above to dynamic

	topTracks = Track.objects.order_by('-upvotes')[:3]
	track1Artist_Id = featTrack1.artist.id
	track2Artist_Id = featTrack2.artist.id
	track3Artist_Id = featTrack3.artist.id


	return render(
		request,
		'index.html',
		context = {	'featTrack1': featTrack1,
					'featTrack2': featTrack2,
				  	'featTrack3': featTrack3,
				  	'track1Artist_Id': track1Artist_Id,
  				  	'track2Artist_Id': track2Artist_Id,
				  	'track3Artist_Id': track3Artist_Id,
		  			'tracks': topTracks,
				  	'yesterdayTrack': yesterdayTrack,
				  	'yesterdayLyric1': yesterdayLyrics[0],
				  	'yesterdayLyric2': yesterdayLyrics[1],
					'audio1': "track_default.mp3",
					'audio2': "track_default.mp3",
					'audio3': "track_default.mp3",
					'yesterdayAudio': "track_default.mp3",
				},
	)

def track(request):
	thisArtist = Artist.objects.get(id = '4c8b7e638ce24032ac6eb8225eafa76a')
	thisTrack = Track.objects.get(artist_id = thisArtist.id)
	# lyric1 = Lyrics.objects.get(id = 'd40bd2d5970a4760b7a7ea56e7628759')
	# comment1 = LyricComment.objects.get(id = 'ec4862f401974ba4ba592ff9c0be1794')
	# lyric2 = Lyrics.objects.get(id = 'd40bd2d5970a4760b7a7ea56e7628759')
	# comment2 = LyricComment.objects.get(id = 'ec4862f401974ba4ba592ff9c0be1794')


	# if request.method == 'POST':
	# 	comment1 = CommentForm(request.POST)
	# 	if comment1.is_valid():
	# 		comment1 = comment1.cleaned_data['comment1'];
	# 		TrackComment1 = TrackComment1 (upvotes=0, text=comment1)
	# 		TrackComment1.save()

	# 		return render(request, 'soundtrack.html')
	# else:
	# 	comment1 = CommentForm()
	# return render(
	# 	request,
	# 	'soundtrack.html',
	# 	context = {
	# 	'comment1': comment1
	# 	},
	# )

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

@login_required
def getTrackInfo(request, pk):
	track = get_object_or_404(Track, pk = pk)
	commentPostURL = '/spitfire/soundtrack/' + str(track.id) + '/comment'
	if request.method == 'GET' or 'POST':
		return render(request, 'soundtrack.html', {'track': track, 'commentPostURL': commentPostURL})

@login_required
def getArtistInfo(request, pk):
	artist = get_object_or_404(Artist, pk = pk)
	if request.method == 'GET':
		return render(request, 'profile.html', {'artist': artist})

@login_required
def getLyricsInfo(request, pk):
	track = get_object_or_404(Track, pk = pk)
	if request.method == 'GET':
		return render(request, 'lyrics-sync.html', {'track': track})
