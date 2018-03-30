from django.db import models

# Create your models here.


class Market(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    latitude = models.IntegerField()
    longitude = models.IntegerField()
    type = models.CharField(max_length=10,choices=(("UB","Urban"),("RU","Rural"),))