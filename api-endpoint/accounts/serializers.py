from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

class CreateUserSerializer(serializers.ModelSerializer):
    token = serializers.CharField(read_only=True)
    profile_pic = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ["token","username", "first_name", "password"]
        extra_kwargs = {
            "password": {"write_only": True}  # password cannot be viewed from the endpoint
        }

    def validate(self, attrs):
        email = attrs['username']
        user = User.objects.filter(email=email)
        if user.exists():
            raise serializers.ValidationError("User with username already exists")
        return attrs

    def create(self, validated_data):
        first_name = validated_data['first_name']
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.create_user(username=username, password=password, first_name=first_name)
        user.save()
        return validated_data