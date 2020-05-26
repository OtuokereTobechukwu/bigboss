from django.forms import ModelForm
from .models import Order, Client

class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = ['order_type']