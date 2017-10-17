from django.db import models
import uuid # Required for unique book instances
from django.urls import reverse #Used to generate URLs by reversing the URL patterns

# Create your models here.

class Genre(models.Model):
    """
    Model for music genres (hip hop, R&B, 90s, etc)
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. hip hop, R&B, 90s, etc)")

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Track(models.Model):
    """
    Model for 
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular track across whole library")
    title  = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this track")

    def get_absolute_url(self):
        """
        Returns the url to access a particular artist instance.
        """
        return reverse('track-detail', args=[str(self.id)])

    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
    display_genre.short_description = 'Genre'

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title


class Lyrics(models.Model):
    """
    Model for lyrics
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole library")
    track = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)
    
    def get_genre(self):
        """
        get the genre of the lyrics from the genre of the track
        """
        self.track.display_genre()

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.track.title,self.id)

class Artist(models.Model):
    """
    Model for Users/Artists (for purposes of simplicity we assume all users are potential artists even if they post no tracks)
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    first_joined = models.DateField(null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular artist instance.
        """
        return reverse('artist-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)


class Comment(models.Model):
    """
    Model for 
    """
    text = models.TextField(max_length=1000, help_text="Enter a comment")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole library")

