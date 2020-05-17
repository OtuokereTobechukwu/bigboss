from django.db import models

# Create your models here.
class subscription(models.Model):
    sub_type = models.CharField(max_length=20)


class menu(models.Model):
    menu_name = models.CharField(max_length=20)

    