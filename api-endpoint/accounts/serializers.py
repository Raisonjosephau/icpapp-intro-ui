from django.contrib.auth.models import User
from rest_framework import serializers,response,status


class CreateUserSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(label="Name")

    class Meta:
        model = User
        fields = ["first_name","username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}  # password cannot be viewed from the endpoint
        }

    def validate(self, attrs):
        username = attrs['username']
        user = User.objects.filter(username=username)
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


class ChangePasswordSerializer(serializers.Serializer):
    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)