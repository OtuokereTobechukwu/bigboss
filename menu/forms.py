from django.forms import ModelForm
from .models import Order, Client
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class Orderform(ModelForm):
    class Meta:
        model = Order
        fields = ['order_type']