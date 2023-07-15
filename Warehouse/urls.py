from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import JuiceView


router = DefaultRouter()
router.register('juice', JuiceView)

urlpatterns = router.urls
