from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class menu(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)  
    cust_menu = models.TextField()
    sub_options = ['one-off','weekly','monthly']
    
def __str__(self):

    return f'{self.user.username} Menu'

