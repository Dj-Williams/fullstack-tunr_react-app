from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=255)
    photo_url = models.CharField(max_length=400, null=True, blank=True)
    nationality = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Song(models.Model):
    title = models.CharField(max_length=255)
    album = models.CharField(max_length=255)
    preview_url = models.CharField(max_length=400)
    # The foreign key is in the songs to create the one to many relationship with the artist model.
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='songs')

    def __str__(self):
        return self.title