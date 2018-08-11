from django.db import models

# Create your models here.

class Tweet(models.Model):
	content = models.CharField(max_length=140)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.content)