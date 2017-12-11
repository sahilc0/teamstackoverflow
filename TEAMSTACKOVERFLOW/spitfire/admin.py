from django.contrib import admin

# Register your models here.


from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Contest, FollowRelationship

admin.site.register(Contest)
admin.site.register(TrackComment)
admin.site.register(LyricComment)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Lyrics)
admin.site.register(Track)
admin.site.register(FollowRelationship)
