from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Network(models.Model):
    name = models.CharField(max_length=128)
    broadcast_address = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Device(models.Model):
    name = models.CharField(max_length=128)
    mac_address = models.CharField(max_length=16)
    network = models.ForeignKey(Network, on_delete=models.CASCADE)

    def __str__(self):
        return self.name