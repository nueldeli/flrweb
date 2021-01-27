from django.contrib import admin
from .models import Subs

# Register your models here.
class SubscribeAdmin(admin.ModelAdmin):
	list_display = ('subscriber_first_name', 'subscriber_last_name', 'subscriber_email')


admin.site.register(Subs, SubscribeAdmin)