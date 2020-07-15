from django.contrib import admin
from tweets.models import TweetModel, TweetLikeModel

# Register your models here.
admin.site.register(TweetModel)
admin.site.register(TweetLikeModel)