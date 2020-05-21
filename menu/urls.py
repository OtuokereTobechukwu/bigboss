from django.urls import path
from . import views
from menu.views import menus


urlpatterns = [

    path('menu/',views.menus, name="menus"),
    path('cart/',views.cart, name="cart"),
    path('checkout/',views.checkout, name="checkout"),

] 