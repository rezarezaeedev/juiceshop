from rest_framework.viewsets import ModelViewSet
from .models import Juice, Brand
from .serializers import JuiceSerializer, BrandSerializer



class JuiceView(ModelViewSet):
	queryset = Juice.objects.all()
	serializer_class = JuiceSerializer


class BrandView(ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
