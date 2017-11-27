from django import forms
from django.forms import ModelForm
from .models import Sponsor, Genre, TrackComment, LyricComment, Track, Lyrics, Artist, User

class UserForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=254)
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=40)
    city = forms.CharField(max_length=40)


class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        exclude = ['upvotes', 'id']
        
class CommentForm (forms.ModelForm):
    comment = forms.CharField (max_length=400)
    