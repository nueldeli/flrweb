from django.contrib import admin
from .models import Seedling

# Register your models here.
class SeedlingAdmin(admin.ModelAdmin):
	list_display = ('local_name', 'scientific_name', 'nursery')

admin.site.register(Seedling, SeedlingAdmin)