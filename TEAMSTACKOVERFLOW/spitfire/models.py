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

class TrackComment(models.Model):
    """
    Model for the comments for specified Track
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole site")
    upvotes = models.PositiveIntegerField(default=0)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000, help_text="Enter a comment")
    track = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        """
        return 'Artist %s %s comment %s on %s' % (self.artist.first_name,self.artist.last_name,self.id,self.track.title)

class LyricComment(models.Model):
    """
    Model for the comments to a lyric
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole site")
    upvotes = models.PositiveIntegerField(default=0)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, null=True)
    text = models.TextField(max_length=1000, help_text="Enter a comment")
    lyrics = models.ForeignKey('Lyrics', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """
        """
        return 'Artist %s %s comment %s on %s' % (self.artist.first_name,self.artist.last_name,self.id,self.lyrics.title)

class Track(models.Model):
    """
    Model for track
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular track across whole site")
    title  = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL,null=True)
    lyrics = models.ForeignKey('Lyrics', on_delete=models.SET_NULL,null=True)
    upvotes = models.PositiveIntegerField(default=0)
    TrackComment.track = models.ForeignKey('TrackComment', on_delete=models.SET_NULL,null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this track")
    
    # file should be named trackid_userid_number
    mp3 = models.FileField(default = "user_audio/track_default.mp3",upload_to='user_audio/')

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
        String for representing the track object.
        """
        return self.title


class Lyrics(models.Model):
    """
    Model for lyrics
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole site")
    artist = models.ForeignKey('Artist', on_delete=models.SET_NULL,null=True)
    upvotes = models.PositiveIntegerField(default=0)
    LyricComment.lyrics = models.ForeignKey('LyricComment', on_delete=models.SET_NULL,null=True)
    Track.lyrics = models.ForeignKey('Track', on_delete=models.SET_NULL, null=True)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this track")
    text = models.TextField(max_length=1000, help_text="Enter lyrics", default="Lyrical spiritual lyrics!")

    def display_genre(self):
        """
        get the genre of the lyrics from the genre of the track
        """
        self.track.display_genre()

    def __str__(self):
        """
        String for representing the lyrics object
        """
        return '%s (%s)' % (self.track.title,self.id)

class Artist(models.Model):
    """
    Model for Users/Artists (for purposes of simplicity we assume all users are potential artists even if they post no tracks)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular artist across whole site")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    Track.artist = models.ManyToManyField(Track)
    Lyrics.artist = models.ManyToManyField(Lyrics)

    number_of_followers = models.PositiveIntegerField(default=0)
    # followers = models.ManyToManyField(self, null=True)
    number_following = models.PositiveIntegerField(default=0)
    # following = models.ManyToManyField(self, null=True)

    date_of_birth = models.DateField(null=True, blank=True)
    first_joined = models.DateField(null=True, blank=True)

    # file should be named userid_ppic_number
    propic = models.FileField(default = "user_propics/profile_default.png",upload_to='user_propics/')
    
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

