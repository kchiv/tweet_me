from django.conf.urls import url

from django.views.generic.base import RedirectView
from .views import (
        RetweetView,
        tweet_detail_view,
        tweet_list_view,
        TweetCreateView,
        TweetUpdateView,
        TweetDeleteView
    )

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/')),
    url(r'^search/$', tweet_list_view, name='list'),
    url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail'),
    url(r'^(?P<pk>\d+)/retweet/$', RetweetView.as_view(), name='retweet'),
    url(r'^(?P<pk>\d+)/update/$', TweetUpdateView.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', TweetDeleteView.as_view(), name='delete'),
    url(r'^create/$', TweetCreateView.as_view(), name='create')
]