from django.shortcuts import render
from .models import *


# Create your views here.

def menus(request):
    products = Product.objects.all()
    orders = Order.objects.all()
    #trying to show the price of each product
    
    
    context={'products':products, 'orders':orders}
    return render(request,'menu/menu.html', context)

def cart(request):
    context={}
    return render(request,'menu/cart.html', context)

def checkout(request):
    context={}
    return render(request,'menu/checkout.html', context)
