from django.db import models


class Juice(models.Model):
	flavour = models.CharField(max_length=50)
	ice = models.BooleanField(default=False)
	nic = models.IntegerField() # TODO: Small int field
	capacity = models.IntegerField() # TODO: Small int field
	salt = models.BooleanField(default=False)
	brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
	price = models.IntegerField() 

	# comment, Rate, Star, and Brand class model


class Brand(models.Model):
	name = models.CharField(max_length=50)
	country = models.CharField(max_length=50)

	#  Star, rate, comment

