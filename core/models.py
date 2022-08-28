from django.db import models


class VideoInformation(models.Model):
	title = models.CharField(max_length=255)
	channelTitle = models.CharField(max_length=255)
	description = models.CharField(max_length=512, blank=True)
	videoId = models.CharField(max_length=512, blank=True)
	published_on = models.CharField(max_length=255)
	thumbnail_url = models.CharField(max_length=512, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now=True)
	is_deleted = models.BooleanField(default=False) 