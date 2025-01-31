from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class mobiles(models.Model):
    image=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    origprice=models.IntegerField()
    ram=models.CharField(max_length=30,null=True)
    rom=models.CharField(max_length=30,null=True)
    camera=models.CharField(max_length=100,null=True)
    battery=models.CharField(max_length=100,null=True)
    overview=models.TextField(max_length=3000,null=True)
    is_bestselling=models.BooleanField(null=True,default=False)
    is_deals=models.BooleanField(null=True,default=False)

class Slides(models.Model):
    img=models.ImageField(upload_to='media/')


