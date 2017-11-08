from django import forms
from django.forms import ModelForm
from .models import Sponsor, Genre, TrackComment, LyricComment, Track, Lyrics, Artist, User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = (
            'city', 'date_of_birth', 'image',
        )