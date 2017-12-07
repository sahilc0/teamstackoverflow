from django.shortcuts import render
from django.contrib.auth import authenticate, login

# Create your views here.
from django.contrib.auth.models import User
from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Contest
from .forms import UserForm,TrackForm,TrackCommentForm,LyricCommentForm,LyricsForm,ContestForm,ArtistForm
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
	featTracks = Track.objects.all().filter(featured = True)[:3]
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
			artist.number_of_spits += 1
			title = form.cleaned_data['title']
			genre = form.cleaned_data['genre']
			description = form.cleaned_data['description']
			keywords = form.cleaned_data['keywords']
			image = form.cleaned_data['image']
			file = form.cleaned_data['mp3']
			track = Track(title=title,artist = artist, genre=genre, description=description, keywords=keywords, image = image, mp3=file)
			artist.save()
			track.save()
			return HttpResponseRedirect('/spitfire/profile/'+str(artist.id))
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
		user_form   = UserForm(request.POST)
		artist_form = ArtistForm(request.POST, request.FILES)
		if user_form.is_valid() and artist_form.is_valid():
			first_name = user_form.cleaned_data['first_name']
			last_name = user_form.cleaned_data['last_name']
			username = user_form.cleaned_data['username']
			password = user_form.cleaned_data['password']
			email = user_form.cleaned_data['email']
			city = artist_form.cleaned_data['city']
			image = artist_form.cleaned_data['image']
			description = artist_form.cleaned_data['description']
			user = User.objects.create_user(username, email, password)			
			user.first_name = first_name
			user.last_name = last_name
			user.save()
			artist = Artist(user=user, firstName = first_name, lastName=last_name, city=city)
			artist.image = image
			artist.description = description
			artist.save()
			return HttpResponseRedirect('/spitfire/profile/'+str(artist.id))
	else:
		user_form = UserForm()
		artist_form = ArtistForm()
	return render(
		request,
		'create_profile.html',
		context = {
			'user_form':user_form,
			'artist_form':artist_form,
		},
	)

def getTrackInfo(request,pk):
    if request.method == 'POST':
        if 'submit-lc' in request.POST:
            lyrics = get_object_or_404(Lyrics,pk=pk)
            tid = str(lyrics.Track.id)
            lcform = LyricCommentForm(request.POST)
            if lcform.is_valid():
                artist = (request.user).artist
                text = lcform.cleaned_data['text']
                upvotes = 0
                lyric_comment = LyricComment(upvotes = upvotes,artist=artist,text=text,lyrics=lyrics)
                lyric_comment.save()
        if 'submit-tc' in request.POST:
            track = get_object_or_404(Track,pk=pk)
            tid = pk
            tcform = TrackCommentForm(request.POST)
            if tcform.is_valid():
                artist = (request.user).artist
                text = tcform.cleaned_data['text']
                upvotes = 0
                track_comment = TrackComment(upvotes = upvotes,artist=artist,text=text,track=track)
                track_comment.save()
        return HttpResponseRedirect('/spitfire/soundtrack/'+tid)
    else:
        track = get_object_or_404(Track, pk = pk)
        lyric_comment_form = LyricCommentForm()
        track_comment_form = TrackCommentForm()
    
    return render(request, 'soundtrack.html', {'track': track,'lyric_comment_form':lyric_comment_form,'track_comment_form':track_comment_form})

@login_required
def getArtistInfo(request, pk):
	artist = get_object_or_404(Artist, pk = pk)
	tracks = Track.objects.filter(artist = artist).order_by('-upvotes')

	allLyrics = Lyrics.objects.filter(artist = artist)
	spitTracks = Track.objects.filter(id__in=allLyrics.values('Track'));

	return render(request, 'profile.html', {'artist': artist,'tracks':tracks, 'spitTracks':spitTracks})

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
			lyrics = Lyrics(title=title, artist=artist, Track=track, text=text)
			lyrics.save()
			return HttpResponseRedirect('/spitfire/soundtrack/'+pk)
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


