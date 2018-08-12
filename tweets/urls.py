from django.conf.urls import url

from .views import (
    tweet_detail_view,
    tweet_list_view,
    TweetCreateView
    )

urlpatterns = [
    url(r'^$', tweet_list_view, name='list'),
    url(r'^(?P<pk>\d+)/$', tweet_detail_view, name='detail')
    url(r'^create/$', TweetCreateView.as_view(), name='create')
]