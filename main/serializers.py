from rest_framework import serializers

from .models import Artist, Song


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'title', 'album', 'preview_url', 'artist')


class ArtistSerializer(serializers.ModelSerializer):
    # This serializer is so that we can show the songs when we grab the artist. The songs don't exist on the artist table, so we need to go get them separately.
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Artist
        fields = ('id', 'name', 'photo_url', 'nationality', 'songs')