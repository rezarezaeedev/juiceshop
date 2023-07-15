from rest_framework.serializers import ModelSerializer
from .models import Juice


class JuiceSerializer(ModelSerializer):
	class Meta:
		model = Juice
		fields = '__all__' 
