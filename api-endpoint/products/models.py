from django.db import models
from markets.models import Market
from django.contrib.auth.models import User
# Create your models here.


class DataTable(models.Model):
    tableid = models.IntegerField()
    category = models.CharField(max_length=100)
    phase = models.CharField(max_length=10)



# class MarketLocation(models.Model):
#     name = models.CharField(max_length=30)
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()





class ProductCatalogue(models.Model):
    dataTable = models.ForeignKey(DataTable,related_name="catalogues",on_delete=models.CASCADE)
    code = models.IntegerField()
    itemName = models.CharField(max_length=100)
    previousPrice = models.IntegerField()
    SDP = models.TextField()
    PDC = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    quantity = models.IntegerField()
    UoM = models.CharField(max_length=100)



class Product(models.Model):
    productCatalogue = models.ForeignKey(ProductCatalogue,related_name="products",on_delete=models.CASCADE)
    pcatid = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()
    priceType = models.CharField(max_length=10,default="INR")
    date = models.BigIntegerField()
    remarks = models.CharField(max_length=200,default=" ")
    locationVerified = models.BooleanField(default=False)


