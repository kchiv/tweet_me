from django.contrib import admin

from .forms import TweetModelForm
from .models import Tweet

# Register your models here.

admin.site.register(Tweet)