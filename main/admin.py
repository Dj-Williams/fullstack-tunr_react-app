from django.contrib import admin

# Register your models here.
from main.models import Song, Artist

admin.site.register([Artist, Song])