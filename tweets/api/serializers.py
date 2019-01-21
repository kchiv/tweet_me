from rest_framework import serializers

from tweets.models import Tweet # alternate import - from ..models import Tweet

class TweetModelSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tweet
		fields = [
			'user',
			'content'
		]