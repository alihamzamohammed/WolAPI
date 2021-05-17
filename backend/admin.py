from django.contrib import admin
from .models import Device, Network

# Register your models here.

class DeviceAdmin(admin.ModelAdmin):
    list_display = ('name', 'mac_address', 'network')

class NetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'broadcast_address')

admin.site.register(Device, DeviceAdmin)
admin.site.register(Network, NetworkAdmin)
