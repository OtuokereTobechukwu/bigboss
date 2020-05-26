from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)  
    name = models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    
    def __str__(self):

        return self.name 


class Order(models.Model):
    CHOICE =(
              ('OneOff', 'OneOff'),
              ('Weekly', 'Weekly'),
              ('Monthly', 'Monthly'),
    )
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    order_id = models.CharField(max_length=100, null=True)
    order_type = models.CharField(max_length=100, null=True, default='Monthly', choices=CHOICE)
    def __str__(self):
        return self.order_type


class Product(models.Model):
    CHOICE =(
              ('Rice', 'Rice'),
              ('Beans', 'Beans'),
              ('Sauces', 'Sauces'),
    )
    order_type = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    items = models.CharField(max_length=100, null=True, choices=CHOICE)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):

        return self.items


    def pricing(self):

        return self.price

class DeliveryAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)




    