from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

class CookieJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        # Get access token from cookie
        access_token = request.COOKIES.get(settings.SIMPLE_JWT['AUTH_COOKIE'])
        
        if not access_token:
            return None  # No token found
        
        # Validate the token
        validated_token = self.get_validated_token(access_token)
        user = self.get_user(validated_token)
        return (user, validated_token)