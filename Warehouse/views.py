from rest_framework.viewsets import ModelViewSet
from .models import Juice, Brand
from .serializers import JuiceSerializer, BrandSerializer
from .permissions import IsSuperUser
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated



class JuiceView(ModelViewSet):
	queryset = Juice.objects.all()
	serializer_class = JuiceSerializer
	permission_classes = [IsSuperUser]
	# authentication_classes=[]


class BrandView(ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	permission_classes = [IsSuperUser]
	# authentication_classes=[JWTAuthentication]
