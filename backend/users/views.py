from rest_framework import (
    generics, 
    permissions, 
    status
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .serializers import (
    UserRegistrationSerializer,
    CustomTokenObtainPairSerializer,
    UserProfileSerializer
)


class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginAPIView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    # def post(self, request, *args, **kwargs):
    #     # Validate credentials (e.g., using a serializer)
    #     username = request.data.get('username')
    #     password = request.data.get('password')
    #     user = authenticate(username=username, password=password)
        
    #     if not user:
    #         return Response({'error': 'Invalid credentials'}, status=401)

    #     # Generate tokens
    #     refresh = RefreshToken.for_user(user)
    #     access_token = str(refresh.access_token)
    #     refresh_token = str(refresh)

    #     # Create response
    #     response = Response(
    #         {'message': 'Login successful', 'user_id': user.id},
    #         status=status.HTTP_200_OK,
    #     )

    #     # Set cookies with tokens
    #     response.set_cookie(
    #         key=settings.SIMPLE_JWT['AUTH_COOKIE'],
    #         value=access_token,
    #         expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
    #         secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
    #         httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
    #         samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
    #     )
    #     response.set_cookie(
    #         key='refresh_token',
    #         value=refresh_token,
    #         expires=settings.SIMPLE_JWT['REFRESH_TOKEN_LIFETIME'],
    #         secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
    #         httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
    #         samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
    #     )

    #     return response

class CookieTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Get refresh token from cookie
        refresh_token = request.COOKIES.get('refresh_token')
        request.data['refresh'] = refresh_token

        # Generate new access token
        response = super().post(request, *args, **kwargs)
        new_access_token = response.data.get('access')

        # Update the access token cookie
        if new_access_token:
            response.set_cookie(
                key=settings.SIMPLE_JWT['AUTH_COOKIE'],
                value=new_access_token,
                expires=settings.SIMPLE_JWT['ACCESS_TOKEN_LIFETIME'],
                secure=settings.SIMPLE_JWT['AUTH_COOKIE_SECURE'],
                httponly=settings.SIMPLE_JWT['AUTH_COOKIE_HTTP_ONLY'],
                samesite=settings.SIMPLE_JWT['AUTH_COOKIE_SAMESITE'],
            )
        return response

class UserLogoutAPIView(generics.GenericAPIView):
    def post(self, request):
        response = Response({'message': 'Logged out'})
        response.delete_cookie(settings.SIMPLE_JWT['AUTH_COOKIE'])
        response.delete_cookie('refresh_token')
        return response
    
class UserProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user