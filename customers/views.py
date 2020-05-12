from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.

def landing(request):
    context={}
    return render(request,'customers/landing.html', context)

def register(request):
    if request.method =="POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Dear {username}, your account has been created!')
            return redirect('menu')
        
    else:
        form = UserRegisterForm()
    return render(request, 'customers/register.html', {'form': form})

