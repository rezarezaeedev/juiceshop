from django.contrib import admin
from .models import Juice, Brand


@admin.register(Juice)
class JuiceAdmin(admin.ModelAdmin):
	pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
	pass
