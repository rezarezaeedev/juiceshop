from rest_framework.authtoken import views
from django.urls import path
from .views import registeration_view, logout_view

urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('register/', registeration_view),
    path('logout/', logout_view),
]
