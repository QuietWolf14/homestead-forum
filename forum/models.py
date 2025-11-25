from django.db import models
from django.conf import settings
from django.utils import timezone


class ForumGroup(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Forum(models.Model):
    name = models.CharField(null=False, blank=False, max_length=500)
    description = models.CharField(null=True, blank=True,max_length=2000)
    forum_group = models.ForeignKey(ForumGroup, null=False, blank=False, on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)
    last_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Post(models.Model):
    forum = models.ForeignKey(Forum, null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(null=False, blank=False, max_length=2000)
    text = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    post = models.ForeignKey(Post, null=False, blank=False, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField(null=False, blank=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)