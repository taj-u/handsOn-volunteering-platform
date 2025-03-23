from django.urls import path, include

# jwt
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import get_routes

from users.views import (
    UserRegistrationView,
    UserLoginAPIView,
    UserLogoutAPIView,
    UserProfileAPIView,
    CookieTokenRefreshView,
)
urlpatterns = [
    path('', get_routes, name='routes'),
    path('auth/register', UserRegistrationView.as_view(), name='user-register'),
    path('auth/login/', UserLoginAPIView.as_view(), name='user-login'),
    path('auth/logout', UserLogoutAPIView.as_view(), name='user-logout'),
    path('auth/token/refresh', CookieTokenRefreshView.as_view(), name='token_refresh'),      # JWT token refresh using cookie
    path('users/me', UserProfileAPIView.as_view(), name='user-profile'),
]