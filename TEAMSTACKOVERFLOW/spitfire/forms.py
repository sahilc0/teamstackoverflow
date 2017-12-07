from django import forms
from django.forms import ModelForm
from .models import Contest, Genre, TrackComment, LyricComment, Track, Lyrics, Artist, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name' ,'password','email']

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['city','image','description']

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ['artist','featured','upvotes', 'id']
        
class TrackCommentForm (forms.ModelForm):
    class Meta:
        model = TrackComment
        exclude = ['upvotes', 'id','artist','track']

class LyricCommentForm(forms.ModelForm):
    class Meta:
        model = LyricComment
        exclude = ['upvotes', 'id','artist','lyrics']        

class LyricsForm(forms.ModelForm):
    class Meta:
        model = Lyrics
        exclude = ['upvotes', 'id','genre','Track','artist']

class ContestForm(forms.ModelForm):
    class Meta:
        model = Contest
        exclude = ['sponsor']
