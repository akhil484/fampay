from django.shortcuts import render

from django.http import HttpResponse
import requests
import json
import os
from core.models import VideoInformation
from core.serializers import VideoInformationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def getResponse(request):
    params = {'part':'snippet','maxResult':10000, 'publishedAfter':'2019-01-01T00:00:00Z', 'q':'cricket'}
    response = requests.get("https://www.googleapis.com/youtube/v3/search?key={}",params=params)
    data=json.loads(response.text)
    for d in data['items']:
        videoID = d['id']['videoId']
        title = d['snippet']['title']
        description = d['snippet']['description']
        publishedAt = d['snippet']['publishedAt']
        thumbnails = d['snippet']['thumbnails']
        channelTitle = d['snippet']['channelTitle']
        try:
            info_obj = VideoInformation.objects.get(videoId=videoID)
        except:
            info_obj = VideoInformation()
        info_obj.title = title
        info_obj.channelTitle = channelTitle
        info_obj.description = description
        info_obj.videoId = videoID
        info_obj.published_on = publishedAt
        info_obj.thumbnail_url = json.dumps(thumbnails)
        print(title)
        info_obj.save()


    return HttpResponse(data['items'])


class VideoList(APIView):
    """
    List of videos.
    """
    paginate_by = 10
    def get(self, request, format=None):
        videos = VideoInformation.objects.filter(is_deleted=False).order_by('-published_on')
        serializer = VideoInformationSerializer(videos, many=True)
        return Response(serializer.data)
