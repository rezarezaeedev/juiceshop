from django.contrib import admin
from .models import Juice, Brand


@admin.register(Juice)
class JuiceAdmin(admin.ModelAdmin):
	list_display = ['flavour', 'get_brand_string', 'capacity', 'nic' ,'salt', 'ice', ]
	list_display_links = list_display


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	list_display = ['name', 'country']
	list_display_links = list_display
	
