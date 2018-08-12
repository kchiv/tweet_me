from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

from .models import Tweet

from .forms import TweetModelForm

# Create your views here.

class TweetCreateView(CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'


def tweet_detail_view(request, pk):
	obj = get_object_or_404(Tweet, pk=pk) #GET from database
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