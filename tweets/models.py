import re

from django.conf import settings
from django.urls import reverse
from django.db import models
from django.db.models.signals import post_save
from django.utils import timezone

from hashtags.signals import parsed_hashtags
from .validators import validate_content

# Create your models here.

class TweetManager(models.Manager):
	def retweet(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj
		qs = self.get_queryset().filter(
				user=user, parent=og_parent
				).filter(
					timestamp__year=timezone.now().year,
					timestamp__month=timezone.now().month,
					timestamp__day=timezone.now().day,
				)
		if qs.exists():
			return None
		obj = self.model(
				parent = og_parent,
				user = user,
				content = parent_obj.content,
			)
		obj.save()
		return obj

class Tweet(models.Model):
	parent = models.ForeignKey('self', blank=True, null=True)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	content = models.CharField(max_length=140, validators=[validate_content])
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	objects = TweetManager()

	def __str__(self):
		return str(self.content)

	def get_absolute_url(self):
		return reverse('tweet:detail', kwargs={'pk':self.pk})

	class Meta:
		ordering = ['-timestamp']


def tweet_save_receiver(sender, instance, created, *args, **kwargs):
	if created and not instance.parent:
		# if parent exists (retweet) do not execute
		# notify a user
		user_regex = r'@(?P<username>[\w.@+-]+)'
		usernames = re.findall(user_regex, instance.content)


		hash_regex = r'#(?P<hashtag>[\w\d-]+)'
		hashtags = re.findall(hash_regex, instance.content)
		parsed_hashtags.send(sender=instance.__class__, hashtag_list=hashtags)


post_save.connect(tweet_save_receiver, sender=Tweet)


