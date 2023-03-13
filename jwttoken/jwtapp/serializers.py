from rest_framework import serializers
from .models import User, token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'user_name']


class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = token
        fields = '__all__'
