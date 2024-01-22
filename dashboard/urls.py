from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExternalResourceAPIView, LogoutView, UserProfileView, CreateUserView

router = DefaultRouter()

urlpatterns = [
    path('external/', ExternalResourceAPIView.as_view(), name="external"),
    path('user/', UserProfileView.as_view(), name="user_log"),
    path('create_user/', CreateUserView.as_view(), name="create_user"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
