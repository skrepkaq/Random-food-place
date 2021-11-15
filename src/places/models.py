import time
from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    uses = models.IntegerField(default=0)
    time = models.IntegerField(default=time.time())


class Place(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    categories = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=20)
