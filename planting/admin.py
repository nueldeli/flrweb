from django.contrib import admin
from .models import PlantingProgram

# Register your models here.
class PlantingProgramAdmin(admin.ModelAdmin):
	list_display = ('program_name', 'program_date')

admin.site.register(PlantingProgram, PlantingProgramAdmin)