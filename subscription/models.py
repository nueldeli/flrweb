from django.db import models
from django.urls import reverse

# Create your models here.
class Subs(models.Model):
	subscriber_first_name = models.CharField(max_length=250)
	subscriber_last_name = models.CharField(max_length=250)
	subscriber_email = models.EmailField(max_length=255)
	subscribe_date = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('home')