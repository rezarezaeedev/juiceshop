from rest_framework.viewsets import ModelViewSet
from .models import Juice
from .serializers import JuiceSerializer



class JuiceView(ModelViewSet):
	queryset = Juice.objects.all()
	serializer_class = JuiceSerializer

