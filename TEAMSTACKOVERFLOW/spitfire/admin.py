from django.contrib import admin

# Register your models here.


from .models import Genre, TrackComment, LyricComment, Track, Lyrics, Artist, Sponsor

admin.site.register(Sponsor)
admin.site.register(TrackComment)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(LyricComment)
admin.site.register(Lyrics)
admin.site.register(Track)