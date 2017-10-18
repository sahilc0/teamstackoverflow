from django.contrib import admin

# Register your models here.


from .models import Track, Artist, Genre, Comment, Lyrics

admin.site.register(Track)
admin.site.register(Artist)
admin.site.register(Genre)
admin.site.register(Comment)
admin.site.register(Lyrics)