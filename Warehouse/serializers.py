from rest_framework.serializers import ModelSerializer
from .models import Juice, Brand


class JuiceSerializer(ModelSerializer):
	class Meta:
		model = Juice
		fields = '__all__' 
		depth = 1


class BrandSerializer(ModelSerializer):
	class Meta:
		model = Brand
		fields = '__all__' 
		depth = 1
