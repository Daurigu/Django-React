from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class TweetLikeModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("TweetModel", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetModel(models.Model):
    parent = models.ForeignKey('TweetModel', null=True, on_delete = models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name='tweet_like', blank=True, through='TweetLikeModel')
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='images/', null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering: ['-id']


