from django.urls import path
from . import views
from menu import views as menu_view



urlpatterns = [

    path('',views.landing, name="landing"),
    path('register/',views.register, name='register'),
    path('menu/',menu_view.menus, name='menu'),

] 