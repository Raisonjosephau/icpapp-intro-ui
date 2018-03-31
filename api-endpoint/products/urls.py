from django.urls import path,include
from .views import CreateProductCatalogueView,CreateProductView,CreateDataTableView,FullProductListView,UpdateProductView
urlpatterns = [
    path('addproductcat/',CreateProductCatalogueView.as_view()),
    path('addproduct/',CreateProductView.as_view()),
    path('adddatatable/',CreateDataTableView.as_view()),
    path('listproducts/',FullProductListView.as_view()),
    path('updateproduct/',UpdateProductView.as_view()),
]