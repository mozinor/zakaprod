from __future__ import unicode_literals
from django.db import models
from django.db.models import permalink

# Create your models here.


class Article(models.Model):
    article_title = models.CharField(max_length=200, db_index=True)
    article_content = models.TextField()
    article_date = models.DateTimeField(auto_now_add=True)
    genre = models.ForeignKey('news.Genre')

    def __unicode__(self):
        return '%s' % self.article_title

    @permalink
    def get_absolute_url(self):
        return 'view_article_post', None, {'slug':self.slug}


class Genre(models.Model):
    genre_title = models.CharField(max_length=50, db_index=True)
    slug = models.CharField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.genre_title

    @permalink
    def get_absolute_url(self):
        return 'view_genre_post', None, {'slug':self.slug}
