from rest_framework.viewsets import ModelViewSet
from .models import Juice, Brand
from .serializers import JuiceSerializer, BrandSerializer
from .permissions import IsSuperUser



class JuiceView(ModelViewSet):
	queryset = Juice.objects.all()
	serializer_class = JuiceSerializer
	permission_classes = [IsSuperUser]


class BrandView(ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	permission_classes = [IsSuperUser]
