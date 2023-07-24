from rest_framework.viewsets import ModelViewSet
from .models import Juice, Brand
from .serializers import JuiceSerializer, BrandSerializer
from .permissions import IsSuperUserOrReadOnly
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class JuiceView(ModelViewSet):
	queryset = Juice.objects.all()
	serializer_class = JuiceSerializer
	permission_classes = [IsSuperUserOrReadOnly]
	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ['flavour', 'brand', 'brand__country', 'brand__name', 'salt' , 'nic' ,'capacity']
	search_fields = ['flavour']
	ordering_fields = ['price', 'capacity' ,'nic', 'salt' ,'ice', ]
	ordering = ['flavour', 'brand__name' ,'nic', 'salt' ,'ice', 'price']


class BrandView(ModelViewSet):
	queryset = Brand.objects.all()
	serializer_class = BrandSerializer
	permission_classes = [IsSuperUserOrReadOnly]
	authentication_classes=[JWTAuthentication]

	filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
	filterset_fields = ['name', 'country']
	search_fields = ['name', 'country']
	ordering_fields = ['name', 'country']
	ordering = ['name', 'country']
