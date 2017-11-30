from django.db import models
import uuid # Required for unique book instances
from django.urls import reverse #Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Contest(models.Model):
    """
    Model for sponsors for contests
    """
    sponsor = models.ForeignKey('Artist',on_delete=models.CASCADE)
    name = models.CharField (max_length=200)
    description = models.CharField (max_length=2000)
    image = models.FileField(upload_to='sponsor/', default='sponsor/sponsor_default.png')
    reward = models.PositiveIntegerField(default = 0)
    track = models.ForeignKey('Track', related_name = 'contest',on_delete=models.CASCADE)

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.name, self.description)

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
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, help_text="Enter a comment")
    track = models.ForeignKey('Track', on_delete=models.CASCADE)

    def __str__(self):
        """
        """
        return 'Artist %s %s comment %s on %s' % (self.artist.firstName,self.artist.lastName,self.id,self.track.title)

class LyricComment(models.Model):
    """
    Model for the comments to a lyric
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole site")
    upvotes = models.PositiveIntegerField(default=0)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    text = models.TextField(max_length=1000, help_text="Enter a comment")
    lyrics = models.ForeignKey('Lyrics', on_delete=models.CASCADE)

    def __str__(self):
        """
        """
        # return 'Artist %s %s comment on %s' % (self.artist.firstName,self.artist.lastName,self.lyrics.title)
        return self.text

class Track(models.Model):
    """
    Model for track
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular track across whole site")
    title = models.CharField(max_length=200)
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    upvotes = models.PositiveIntegerField(default=0)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this track")
    description = models.TextField(blank=True, max_length=300)
    keywords = models.TextField(blank = True, max_length=30)
    featured = models.BooleanField(default=False)
    image = models.FileField(upload_to='track_pics/', default='track_pics/trackpic_default.jpg')
    mp3 = models.FileField(upload_to='user_audio/', default='user_audio/track_default.mp3')

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

    def top_lyrics(self):
        return Lyrics.objects.filter(Track=self.id).order_by('-upvotes')

    def __str__(self):
        """
        String for representing the track object.
        """
        return self.title

    def createTrack(self, id, title, artist, upvotes, genre, description, keywords):
        track = self.create(title=title, artist=artist, upvotes=upvotes, genre=genre, description=description, keywords=keywords)
        return track

class Lyrics(models.Model):
    """
    Model for lyrics
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular lyrics across whole site")
    artist = models.ForeignKey('Artist', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, default="Some Terrific Lyrics")
    upvotes = models.PositiveIntegerField(default=0)
    Track = models.ForeignKey('Track', on_delete=models.CASCADE)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this track")
    text = models.TextField(max_length=1000, help_text="Enter lyrics", default="Lyrical spiritual lyrics!")

    def display_genre(self):
        """
        get the genre of the lyrics from the genre of the track
        """
        self.track.display_genre()

    def top_comments(self):
        return LyricComment.objects.filter(lyrics=self.id).order_by('-upvotes')

    def __str__(self):
        """
        String for representing the lyrics object
        """
        return self.title


class Artist(models.Model):
    """
    Model for Users/Artists (for purposes of simplicity we assume all users are potential artists even if they post no tracks)
    """
    user = models.OneToOneField(User, related_name = 'artist', on_delete=models.CASCADE)
    # set the default value
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular artist across whole site")
    firstName = models.CharField(max_length=100, default = "Firstname")
    lastName = models.CharField(max_length=100, default = "Lastname")
    city = models.CharField(max_length=100, null=True)
    description = models.TextField(max_length=2000)
    number_of_spits = models.PositiveIntegerField(default=0)
    number_of_followers = models.PositiveIntegerField(default=0)
    number_of_following = models.PositiveIntegerField(default=0)
    date_of_birth = models.DateField(null=True)
    first_joined = models.DateField(null=True)
    twitter_link = models.CharField(max_length=100,blank=True,null=True)
    instagram_link = models.CharField(max_length=100,blank=True, null=True)
    soundcloud_link = models.CharField(max_length=100,blank=True, null=True)
    image = models.FileField(upload_to='user_propics/', default='user_propics/profile_default.png')

    def full_name(self):
        """
        Returns the full name of this Artist.
        """
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
        """
        Returns the url to access a particular artist instance.
        """
        return reverse('artist-detail', args=[str(self.id)])

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.lastName, self.firstName)
