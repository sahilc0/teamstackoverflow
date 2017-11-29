from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.contrib.auth.models import User
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Contest
from .forms import UserForm,TrackForm,TrackCommentForm,LyricCommentForm,LyricsForm,ContestForm
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse #this line might not be needed
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

def search(request):
	search_field = request.GET.get('search_field', None)
	search_results = Track.objects.filter(title__contains=search_field) | Track.objects.filter(description__contains=search_field) | Track.objects.filter(keywords__contains=search_field)

	return render(request, "search_result.html", context = {'tracks': search_results,},)

def index(request):
	featTracks = Track.objects.all().filter(featured = True)
	topTracks = Track.objects.order_by('-upvotes')[:3]
	return render(
		request,
		'index.html',
		context = {	'featTracks': featTracks,
		  			'tracks': topTracks,					
				},
	)

@login_required
def upload(request):
	if request.method == 'POST':
		user = request.user
		form = TrackForm(request.POST, request.FILES)
		if form.is_valid():
			artist = user.artist
			title = form.cleaned_data['title']
			genre = form.cleaned_data['genre']
			description = form.cleaned_data['description']
			keywords = form.cleaned_data['keywords']
			image = form.cleaned_data['image']
			file = form.cleaned_data['mp3']
			track = Track(title=title,artist = artist, genre=genre, description=description, keywords=keywords, image = image, mp3=file)
			track.save()
			return render(request, 'soundtrack.html', {'track': track})
	else:
		form = TrackForm()
	return render(request, 'trackForm.html', {'form': form})

def contest(request):
	"""
	put stuff here
	"""
	contests = Contest.objects.all()

	return render(
		request,
		'contest.html',
		context= {'contests':contests,}
	)

@login_required
def create_contest(request):
	if request.method == 'POST':
		form = ContestForm(request.POST)
		if form.is_valid():
			sponsor = request.user
			name = form.cleaned_data['name']
			description = form.cleaned_data['description']
			image = form.cleaned_data['image']
			contest = Contest(sponsor = sponsor,name=name,description=description,image=image)
			contest.save()
			return render(request,'contest.html')
	else:
		form = ContestForm()
	return render(request, 'createContest.html', {'form':form})

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
			# image = user_form.cleaned_data['image']
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			#we can substitute the bottom code with a @receiver decorator
			artist = Artist(user=user, firstName = user.first_name, lastName=user.last_name, city=city,)
			# add image = image to above when that gets fixed
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

def getTrackInfo(request, pk):
	track = get_object_or_404(Track, pk = pk)
	#commentPostURL = '/spitfire/soundtrack/' + str(track.id) + '/comment'
	return render(request, 'soundtrack.html', {'track': track})

@login_required
def getArtistInfo(request, pk):
	artist = get_object_or_404(Artist, pk = pk)
	tracks = Track.objects.filter(artist = artist).order_by('-upvotes')
	return render(request, 'profile.html', {'artist': artist,'tracks':tracks})

@login_required
def getLyricsInfo(request, pk):
	track = get_object_or_404(Track, pk = pk)
	if request.method == 'POST':
		user = request.user
		form = LyricsForm(request.POST)
		if form.is_valid():
			artist = user.artist
			title = form.cleaned_data['title']
			text = form.cleaned_data['text']
			lyrics = Lyrics(title=title, artist=artist, track=track, text=text)
			lyrics.save()
			return render(request, 'soundtrack.html', {'track': track})
	else:
		form = LyricsForm()
	return render(request, 'lyrics-sync.html', {'track':track,'form': form})

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


# this is just here to make sure soundtrack doesn't crash!
def create_comment(request):
	track = get_object_or_404(Track, pk = pk)
	if request.method == 'POST':
		form = TrackCommentForm(request.POST)
		if form.is_valid():
			artist = request.user
			text = form.cleaned_data['text'];
			track_comment = TrackComment (upvotes=0, text=text, track=track, artist=artist)
			track_comment.save()
			# TODO:
			# this should return to (or render) the original
			# page from which it was originally
			# called, not just any old soundtrack page
			return render(request, 'soundtrack.html', {'track':track})
	else:
		form = CommentForm()

	# TODO:
	# we want this render to be for the comment creation page
	# or somehow figure out how to use this function (perhaps
	# as a class-based view), in the actual soundtrack page
	return render(
		request,
		'soundtrack.html',
		context = {
		'form': form
		},
	)

# TODO: 
# what needs to be figured out to create track and lyric
# comments is how it is that you determine what track
# is being commented on, maybe this gets passed to the form
# or maybe there can be some helper function
@login_required
def create_track_comment (request,pk):
	track = get_object_or_404(Track, pk = pk)
	if request.method == 'POST':
		form = TrackCommentForm(request.POST)
		if form.is_valid():
			artist = request.user
			text = form.cleaned_data['text'];
			track_comment = TrackComment (upvotes=0, text=text, track=track, artist=artist)
			track_comment.save()
			# TODO:
			# this should return to (or render) the original
			# page from which it was originally
			# called, not just any old soundtrack page
			return render(request, 'soundtrack.html', {'track':track})
	else:
		form = CommentForm()

	# TODO:
	# we want this render to be for the comment creation page
	# or somehow figure out how to use this function (perhaps
	# as a class-based view), in the actual soundtrack page
	return render(
		request,
		'soundtrack.html',
		context = {
		'form': form
		},
	)

# TODO:
# once the TODOs in the create_track_comment have been 
# cleared up, the resulting code can be easily ported to
# fill in create_lyric_comment. the only difference will be
# that track will be lyric, and the form being delivered
# will be different, the model being created will be 
# different
# @login_required
# def create_lyric_comment(request):