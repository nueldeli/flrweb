from django.contrib import admin
from .models import PlantingProgram, Item

# Register your models here.
class PlantingProgramAdmin(admin.ModelAdmin):
	list_display = ('program_name', 'program_date')

class ItemAdmin(admin.ModelAdmin):
	list_display = ('item_local_name',)	

admin.site.register(Item, ItemAdmin)
admin.site.register(PlantingProgram, PlantingProgramAdmin)