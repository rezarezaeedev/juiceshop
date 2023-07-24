from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JuiceView, BrandView
app_name = 'warehouse'



router = DefaultRouter()
router.register('juice', JuiceView)
router.register('brand', BrandView)

urlpatterns = [
	path('', include(router.urls)),
]
