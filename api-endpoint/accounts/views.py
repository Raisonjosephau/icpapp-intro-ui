from django.shortcuts import render
from .serializers import CreateUserSerializer,UserChangePasswordSerializer
from rest_framework import generics,permissions
from django.http import HttpResponse
# Create your views here.


class CreateUserView(generics.CreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateUserSerializer


def vrthe(request):
    return(HttpResponse("Raisaaaaaa"))


class UserChangePasswordView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserChangePasswordSerializer
