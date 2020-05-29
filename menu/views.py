from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages 
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


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


def landing(request):
    context={}
    return render(request,'menu/landing.html', context)

def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, your account has been created! Please Log in')
            return redirect('login')
        
    else:
        form = UserRegisterForm()
    return render(request, 'menu/register.html', {'form': form})

@login_required
def myboss(request):
    return render(request, 'menu/myboss.html')



