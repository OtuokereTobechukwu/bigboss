from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Client)
admin.site.register(Subscription)
admin.site.register(Dishes)
admin.site.register(DeliveryAddress)
admin.site.register(OrderItem)