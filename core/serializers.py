from rest_framework import serializers
from core.models import VideoInformation

class VideoInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoInformation
        fields = ['id', 'title', 'channelTitle', 'description', 'published_on', 'thumbnail_url']
