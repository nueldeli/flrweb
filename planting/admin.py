from django.contrib import admin
from .models import PlantingProgram, Item, Order, OrderItem

# Register your models here.
class PlantingProgramAdmin(admin.ModelAdmin):
	list_display = ('program_name', 'program_date')

class ItemAdmin(admin.ModelAdmin):
	list_display = ('item_local_name',)

class OrderAdmin(admin.ModelAdmin):
	list_display = ('user',)

class OrderItemAdmin(admin.ModelAdmin):
	list_display = ('item',)	

admin.site.register(Item, ItemAdmin)
admin.site.register(PlantingProgram, PlantingProgramAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)