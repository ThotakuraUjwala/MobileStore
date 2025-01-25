from django.db import models

# Create your models here.
class bestselling(models.Model):
    image=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    origprice=models.IntegerField()
    
