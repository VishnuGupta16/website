from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.artist + " created "+self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE)# on deleting particular album all song corresponding to it will be deleted
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title