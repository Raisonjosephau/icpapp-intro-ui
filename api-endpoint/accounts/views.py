from django.shortcuts import render
from .serializers import CreateUserSerializer
from rest_framework import generics,permissions
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer
