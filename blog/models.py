from django.db import models
from django.urls import reverse
from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.fields.files import ImageFieldFile, FileField

# Create your models here.
class Post(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	title = models.CharField('Post title' ,max_length=250)
	date_written = models.DateTimeField(auto_now_add=True)
	slug = models.SlugField(max_length=250, unique=True, null=True, blank=True)
	thumbnail_img = models.ImageField('Thumbnail', null=True, blank=True, upload_to='thumbnail/')
	post_snippet = models.TextField('Post snippet', max_length=250, null=True)
	content = RichTextUploadingField(blank=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('post_detail', kwargs={'slug':self.slug})

	def get_post_thumbnail(self):
		if self.thumbnail_img and hasattr(self.thumbnail_img, 'url'):
			return self.thumbnail_img.url
		return ImageFieldFile(instance=None, field=FileField(), name='/media/thumbnail/blog_default.png')



#This function runs when a signal calls it (For slugify-ing the slug)
def slug_generator(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug = unique_slug_generator(instance)

pre_save.connect(slug_generator, sender=Post)
