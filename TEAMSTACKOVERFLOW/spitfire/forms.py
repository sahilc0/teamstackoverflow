from django import forms
from django.forms import ModelForm
from .models import Contest, Genre, TrackComment, LyricComment, Track, Lyrics, Artist, User

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=40)
    city = forms.CharField(max_length=40)
    # image = forms.FileField(required=False)


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
