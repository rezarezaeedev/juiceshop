from rest_framework.authtoken import views
from django.urls import path
# from .views import registeration_view, logout_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    # Related Default DRF token authentication
    # path('login/', views.obtain_auth_token),
    # path('register/', registeration_view),
    # path('logout/', logout_view),

    # Related Django restframeowrk JWT token authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
