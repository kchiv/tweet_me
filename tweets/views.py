from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Tweet
from .mixins import FormUserNeededMixin, UserOwnerMixin

from .forms import TweetModelForm

# Create your views here.

class TweetDeleteView(LoginRequiredMixin, DeleteView):
	model = Tweet
	template_name = 'tweets/delete_confirm.html'
	success_url = reverse_lazy('home')

class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
	queryset = Tweet.objects.all()
	form_class = TweetModelForm
	template_name = 'tweets/update_view.html'
	success_url = '/tweet/'
	login_url = '/admin/'

class TweetCreateView(LoginRequiredMixin, FormUserNeededMixin, CreateView):
	form_class = TweetModelForm
	template_name = 'tweets/create_view.html'
	success_url = '/tweet/create/'
	login_url = '/admin/'

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