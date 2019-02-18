from django.conf import settings
from django.urls import reverse
from django.db import models

from .validators import validate_content

# Create your models here.

class TweetManager(models.Manager):
	def retweet(self, user, parent_obj):
		if parent_obj.parent:
			og_parent = parent_obj.parent
		else:
			og_parent = parent_obj
		qs = self.get_queryset().filter(user=user, parent=parent_obj)
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