from django.shortcuts import render
from rest_framework import generics,permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from .serializers import CreateProductCatalogueSerializer,CreateProductSerializer,CreateDataTableSerializer, ListFullProducts,UpdateProductSerializer
from .models import DataTable,ProductCatalogue,Product

# Create your views here.


class CreateProductCatalogueView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateProductCatalogueSerializer
    queryset = ProductCatalogue.objects.all()


class CreateProductView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateProductSerializer
    queryset = Product.objects.all()

class CreateDataTableView(generics.ListCreateAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateDataTableSerializer
    queryset = DataTable.objects.all()

class FullProductListView(generics.ListAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ListFullProducts
    queryset = DataTable.objects.all()

class UpdateProductView(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdateProductSerializer
    queryset = Product.objects.all()
