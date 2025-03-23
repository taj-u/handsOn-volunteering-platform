from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'skills', 'causes', 'volunteer_hours')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password', 'bio', 'skills', 'causes')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['username'],
            email = validated_data['email'],
            password = validated_data['password'],
            bio = validated_data.get('bio', ''),
            skills = validated_data.get('skills', []),
            causes = validated_data.get('causes', [])
        )
        return user

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'email': self.user.email,
            'bio': self.user.bio,
            'skills': self.user.skills,
            'causes': self.user.causes,
            'volunteer_hours': self.user.volunteer_hours
        })
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'bio', 'skills', 'causes', 'volunteer_hours', 
                 'created_at', 'updated_at')
        read_only_fields = ('email', 'volunteer_hours', 'created_at')