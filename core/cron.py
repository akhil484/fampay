import requests
import json
import os
from core.models import VideoInformation
from django.shortcuts import render
from django.http import HttpResponse
import asyncio
# import the logging library
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)


def getResponse():
    params = {'part':'snippet','maxResult':50, 'publishedAfter':'2019-01-01T00:00:00Z', 'q':'cricket'}
    response = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyA7qBc9uodDSipLGjDzKPIh-sTBOpCZIt0",params=params)
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

        try:
        	info_obj.title = title
        	info_obj.channelTitle = channelTitle
        	info_obj.description = description
        	info_obj.videoId = videoID
        	info_obj.published_on = publishedAt
        	info_obj.thumbnail_url = json.dumps(thumbnails)
        	info_obj.save()
        	logger.info('Cron in Try')
        except:
        	logger.info('Cron in Except')
        	pass