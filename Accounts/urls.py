from django.urls import path
from .views import registeration_view
from rest_framework_simplejwt import views

urlpatterns = [
    path('register/', registeration_view),
    path('api/token/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', views.TokenVerifyView.as_view(), name='token_verify'),
]
