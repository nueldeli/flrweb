from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'slug', 'date_written')

admin.site.register(Post, PostAdmin)