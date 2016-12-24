from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Artist(models.Model):
    artist_name = models.CharField(max_length=70)
    description = models.CharField(max_length=140)
    genre = models.CharField(max_length=30)

    def __str__(self):
        return self.artist_name


class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=100)
    album_rate = models.FloatField(default=0.0)

    def __str__(self):
        return self.album_name


class Song(models.Model):
    song_artist = models.ManyToManyField(Artist)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=100, db_index=True)
    song_pub_date = models.DateField('published_on')
    song_description = models.CharField(max_length=200)
    song_rating = models.FloatField(default=0.0)
    song_link = models.URLField()

    def __str__(self):
        return self.song_title


class Video(models.Model):
    video_artist = models.ForeignKey(Artist)
    video_title = models.CharField(max_length=100, db_index=True)
    video_pub_date = models.DateField('published_on')
    video_description = models.CharField(max_length=200)
    video_rating = models.FloatField(default=0.0)
    video_link = models.URLField()

    def __str__(self):
        return self.video_title


class Comment(models.Model):
    user_email = models.EmailField()
    user_first = models.CharField(max_length=50)
    user_last = models.CharField(max_length=50)
    comment_content = models.CharField(max_length=500)
    aprprt_comment = models.BooleanField(default=False)
    comment_title = models.CharField(max_length=20)

    def __str__(self):
        return self.comment_title



