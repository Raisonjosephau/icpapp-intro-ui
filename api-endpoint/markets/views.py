from django.shortcuts import render
from .serializers import CreateMarketSerializer
from rest_framework import generics,permissions
# Create your views here.

class CreateMarketView(generics.CreateAPIView):
    serializer_class = CreateMarketSerializer
    permission_classes = (permissions.IsAuthenticated)

