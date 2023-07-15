from django.db import models


class Juice(models.Model):
	flavour = models.CharField(max_length=50)
	ice = models.BooleanField(default=False)
	nic = models.IntegerField() # TODO: Small int field
	capacity = models.IntegerField() # TODO: Small int field
	salt = models.BooleanField(default=False)
	brand = models.CharField(max_length=50) # TODO: Brand Class Model
	price = models.IntegerField() 

	# comment, Rate and Brand class model


