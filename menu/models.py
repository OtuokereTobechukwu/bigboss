from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Client(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, blank=True, null=True)  
    name = models.CharField(max_length=200, null=True)
    email =  models.CharField(max_length=200, null=True)
    
    def __str__(self):

        return self.name


class Subscribe(models.Model):
    CHOICE =(
              ('OneOff', 'OneOff'),
              ('Weekly', 'Weekly'),
              ('Monthly', 'Monthly'),
    )
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    sub_id = models.CharField(max_length=100, null=True)
    sub_type = models.CharField(max_length=100, null=True, default='Monthly', choices=CHOICE)

    def __str__(self):
        return self.sub_type


class Dishes(models.Model):
    CHOICE =(
              ('Rice', 'Rice'),
              ('Beans', 'Beans'),
              ('Sauces', 'Sauces'),
              ('Pasta', 'Pasta'),
              ('Proteins', 'Proteins'),
              ('Swallow', 'Swallow'),
    )
    sub_type = models.ForeignKey(Subscribe, on_delete=models.SET_NULL, null=True, blank=True)
    dish_name = models.CharField(max_length=100, null=True, choices=CHOICE)
    #complete = models.BooleanField(default=False)
    price = models.FloatField()
    #image field
    
    def __str__(self):
 
        return self.dish_name


class OrderItem(models.Model):
    dish_name = models.ForeignKey(Dishes, on_delete=models.SET_NULL, null=True)
    sub_type = models.ForeignKey(Subscribe, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)


class DeliveryAddress(models.Model):
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True)
    sub_type = models.ForeignKey(Subscribe, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    state = models.CharField(max_length=200, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.address)




    