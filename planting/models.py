from django.db import models
from django.urls import reverse
from django.db.models.fields.files import ImageFieldFile, FileField

# Create your models here.
class PlantingProgram(models.Model):
	date_created = models.DateTimeField(auto_now_add=True)
	program_date = models.CharField(max_length=50)
	program_name = models.CharField(max_length=200)
	program_location = models.CharField(max_length=100)
	program_area = models.FloatField()
	program_species = models.CharField(max_length=200)
	program_participant = models.CharField(max_length=200)
	program_img = models.ImageField('Program Image', null=True, blank=True, upload_to='program_img/')

	class Meta:
		ordering = ['-date_created']

	def __str__(self):
		return self.program_name + ' | ' + str(self.program_date)

	def get_program_img(self):
		if self.program_img and hasattr(self.program_img, 'url'):
			return self.program_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/program_img/program_img_default.png')

	def get_absolute_url(self):
		return reverse('planting_program_index')