from rest_framework import serializers
from .models import Album, Photo

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['id', 'album', 'title', 'image', 'description', 'created_at', 'updated_at']

class AlbumSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'slug', 'description', 'cover_image', 'created_at', 'updated_at', 'photos']
        read_only_fields = ['slug'] 