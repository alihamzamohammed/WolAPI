from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DeviceSerializer, NetworkSerializer
from .models import Device, Network

# Create your views here.

class DeviceView(viewsets.ModelViewSet):
    serializer_class = DeviceSerializer
    queryset = Device.objects.all()

class NetworkView(viewsets.ModelViewSet):
    serializer_class = NetworkSerializer
    queryset = Network.objects.all()