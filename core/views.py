from django.shortcuts import render

from django.http import HttpResponse
import requests
import json
import os
from core.models import VideoInformation
from core.serializers import VideoInformationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# class VideoList(APIView):
#     """
#     List of videos.
#     """
#     def get(self, request, format=None):
#         videos = VideoInformation.objects.filter(is_deleted=False).order_by('-published_on')
#         serializer = VideoInformationSerializer(videos, many=True)
#         return Response(serializer.data)

class VideoList(generics.ListCreateAPIView):
    """
    List of videos.
    """
    
    queryset = VideoInformation.objects.filter(is_deleted=False).order_by('-published_on')
    serializer_class = VideoInformationSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','description']
    
