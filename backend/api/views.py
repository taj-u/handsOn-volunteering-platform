from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from users.models import CustomUser
from users.serializers import CustomUserSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        'api/',
        'api/auth/login',
        'api/auth/logout',
        'api/auth/register',
        'api/auth//token/refresh',
        'api/users/me',
    ]
    return Response(routes)
