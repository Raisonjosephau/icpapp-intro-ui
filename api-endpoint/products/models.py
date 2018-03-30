from django.db import models
from markets.models import Market
from django.contrib.auth.models import User
# Create your models here.


class DataTable(models.Model):
    tableid = models.IntegerField()
    category = models.CharField(max_length=100,choices=(("EGG","Egg and egg Products"),("STA","Stationary"),))


# class MarketLocation(models.Model):
#     name = models.CharField(max_length=30)
#     latitude = models.IntegerField()
#     longitude = models.IntegerField()


class UserLocation(models.Model):
    name = models.CharField(max_length=30)
    accuracy = models.IntegerField()
    latitude = models.IntegerField()
    longitude = models.IntegerField()


class Product(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dataTable = models.ForeignKey(DataTable,on_delete=models.CASCADE)
    code = models.IntegerField()
    itemName = models.CharField(max_length=100)
    previousPrice = models.IntegerField()
    image = models.ImageField()
    SDP = models.TextField()
    PDC = models.CharField(max_length=100)
    quantity = models.IntegerField()
    UoM = models.CharField(max_length=100)
    price = models.IntegerField()
    priceType = models.CharField(max_length=10)
    date = models.BigIntegerField()
    remarks = models.CharField(max_length=200)
    locationVerified = models.BooleanField(default=False)
    market = models.ForeignKey(Market,on_delete=models.CASCADE)
    userLocation = models.OneToOneField(UserLocation,on_delete=models.CASCADE)


