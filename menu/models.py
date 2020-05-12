from django.db import models

# Create your models here.
class menu(models.Model):
    menu_name = models.CharField(max_length=20)