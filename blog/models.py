#-*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Person(AbstractUser):
#    name = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    mode_restricted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.username

    @property

    def get_rating(self):
        res = 0

        for post in self.post.all():
            res += post.rating

        for comment in self.comment.all():
            res += comment.rating
        return res

    class Meta:
        verbose_name_plural = 'Persons'

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name

class Post(models.Model):
    name = models.CharField(max_length=50)
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="post")
    release_date = models.DateField(default=timezone.now)
    restricted = models.BooleanField(default=False)
    rating = models.IntegerField(default=0)
    text = models.TextField()
    tag = models.ManyToManyField(Tag, related_name="post", blank=True)

    def __unicode__(self):
        return self.name

    @property

    def get_rating(self):
        res = 0

        for like in self.like.all():
            res += 1 if like.plus else -1
        return res

class Comment(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="comment")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment")
    release_date = models.DateField(default=timezone.now)
    rating = models.IntegerField(default=0)
    text = models.TextField()

    def __unicode__(self):
        return self.text

    @property

    def get_rating(self):
        res = 0

        for like in self.like.all():
            res += 1 if like.plus else -1
        return res

class PostPlus(models.Model):
    plus = models.BooleanField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="post_like")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="like")

    def __unicode__(self):
        return 'Plus of ' + self.author.username + ' to post ' + self.post.name

    class Meta:
        verbose_name_plural = 'Post pluses'

class CommentPlus(models.Model):
    plus = models.BooleanField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="comment_like")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="like")

    def __unicode__(self):
        return 'Plus of ' + self.author.username + ' to comment of ' + self.comment.author.username + ' to post ' + self.comment.post.name

    class Meta:
        verbose_name_plural = 'Comment pluses'
