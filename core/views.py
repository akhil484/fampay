from django.shortcuts import render

from django.http import HttpResponse
import requests
import json
import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")



scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def getResponse(request):
    # # Disable OAuthlib's HTTPS verification when running locally.
    # # *DO NOT* leave this option enabled in production.
    # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    # api_service_name = "youtube"
    # api_version = "v3"
    # # client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"
    # api_key = "AIzaSyA7qBc9uodDSipLGjDzKPIh-sTBOpCZIt0"

    # # Get credentials and create an API client
    # flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    #     api_key, scopes)
    # credentials = flow.run_console()
    # youtube = googleapiclient.discovery.build(
    #     api_service_name, api_version, credentials=credentials)

    # request = youtube.search().list(
    #     part="snippet",
    #     maxResults=25,
    #     q="dogs"
    # )
    # response = request.execute()
    params = {'part':'snippet','maxResult':10000, 'publishedAfter':'2019-01-01T00:00:00Z', 'q':'cricket'}
    response = requests.get("https://www.googleapis.com/youtube/v3/search?key=AIzaSyA7qBc9uodDSipLGjDzKPIh-sTBOpCZIt0",params=params)
    data=json.loads(response.text)
    # print(data['items'])
    for d in data['items']:
    	print(d['snippet']['title'])
    return HttpResponse(data['items'])
