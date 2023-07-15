from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JuiceView, BrandView


router = DefaultRouter()
router.register('juice', JuiceView)
router.register('brand', BrandView)


urlpatterns = router.urls
