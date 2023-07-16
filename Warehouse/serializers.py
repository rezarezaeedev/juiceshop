from rest_framework import serializers
from .models import Juice, Brand


class JuiceSerializer(serializers.ModelSerializer):
	salt = serializers.SerializerMethodField()

	def get_salt(self, obj):
		nic=int(obj.nic)
		if nic > 19:
			return True
		return False

	class Meta:
		model = Juice
		fields = '__all__' 


class BrandSerializer(serializers.ModelSerializer):
	class Meta:
		model = Brand
		fields = '__all__' 
		depth = 1
