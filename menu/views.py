from django.shortcuts import render
from .models import menu

# Create your views here.

def menus(request):
    context={}
    return render(request,'menu/menu.html', context)

def cart(request):
    context={}
    return render(request,'menu/cart.html', context)

def checkout(request):
    context={}
    return render(request,'menu/checkout.html', context)

