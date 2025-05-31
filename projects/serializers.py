from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'slug', 'description', 'content', 'created_at', 'updated_at', 
                 'featured_image', 'github_url', 'live_url', 'tags']
        read_only_fields = ['slug'] 