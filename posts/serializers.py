from rest_framework import serializers
from .models import Post
 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'content', 'created_at', 'updated_at', 'featured_image', 'tags']
        read_only_fields = ['slug'] 