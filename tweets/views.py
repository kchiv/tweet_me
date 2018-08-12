from django.shortcuts import render

from .models import Tweet

# Create your views here.


def tweet_detail_view(request, pk):
	obj = Tweet.objects.get(pk=pk) #GET from database
	context = {
		'object': obj
	}
	return render(request, 'tweets/detail_view.html', context)


def tweet_list_view(request):
	queryset = Tweet.objects.all()
	context = {
		'object_list': queryset
	}
	return render(request, 'tweets/list_view.html', context)