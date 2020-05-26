from django.shortcuts import render
from .models import *


# Create your views here.

def menus(request):
    products = Product.objects.all()
    #trying to show the price of each product
    
    #product_price = Product.objects.get()
    context={'products':products, 'product_price': product_price}
    return render(request,'menu/menu.html', context)

def cart(request):
    context={}
    return render(request,'menu/cart.html', context)

def checkout(request):
    context={}
    return render(request,'menu/checkout.html', context)


