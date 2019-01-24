from django.db.models import Q
from rest_framework import generics

from tweets.models import Tweet
from .serializers import TweetModelSerializer

class TweetListAPIView(generics.ListAPIView):
	serializer_class = TweetModelSerializer

	def get_queryset(self, *args, **kwargs):
		queryset = Tweet.objects.all()
		query = self.request.GET.get('q', None)
		if query is not None:
			queryset = queryset.filter(
						Q(content__icontains=query) |
						Q(user__username__icontains=query)
						)
		return queryset