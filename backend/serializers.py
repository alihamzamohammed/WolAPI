from rest_framework import serializers
from .models import Device, Network

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('name', 'mac_address', 'network')

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ('name', 'broadcast_address')