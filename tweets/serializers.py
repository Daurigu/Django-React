from rest_framework import serializers
from tweets.models import TweetModel


ACTIONS = ['like', 'unlike', 'retweet']

class ActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()

    def validate_action(self, value):
        if value in ACTIONS:
            return value
        else:
            raise serializer.ValidationError('You most enter a real action, try again')


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = ['content']

    def validate_content(self, value):
        if len(value) > 240:
            raise serializers.ValidationError('To Long bro')
        return value
