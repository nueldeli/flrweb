from django.db import models
from django.urls import reverse 
from django.db.models.fields.files import ImageFieldFile, FileField

# Create your models here.
class Seedling(models.Model):
	date_input = models.DateTimeField(auto_now_add=True)
	local_name = models.CharField(max_length=100)
	scientific_name = models.CharField(max_length=100)
	category = models.CharField(max_length=100)
	origin = models.CharField(max_length=100)
	nursery = models.CharField(max_length=100)
	remarks = models.CharField(max_length=200)
	description = models.TextField()
	quantity = models.IntegerField()
	seedling_img = models.ImageField('Seedling Image', null=True, blank=True, upload_to='seedling_img/')

	class Meta:
		ordering = ['-date_input']

	def __str__(self):
		return self.local_name + ' | ' + self.scientific_name

	def get_seedling_img(self):
		if self.seedling_img and hasattr(self.seedling_img, 'url'):
			return self.seedling_img.url 
		return ImageFieldFile(instance=None, field=FileField(), name='/media/seedling_img/seedling_default_img.png')

	def get_absolute_url(self):
		return reverse('seedling_index')
