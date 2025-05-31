from rest_framework import serializers
from .models import Profile
 
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'name', 'title', 'bio', 'email', 'phone', 'location', 'website', 'github', 'linkedin', 'avatar', 'created_at', 'updated_at'] 