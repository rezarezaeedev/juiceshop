from django.urls import path
from .views import registeration_view
from rest_framework_simplejwt import views
app_name = 'accounts'


urlpatterns = [
    path('register/', registeration_view, name = 'register'),
    path('login/', views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh-token/', views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/verify-token/', views.TokenVerifyView.as_view(), name='token_verify'),
]
