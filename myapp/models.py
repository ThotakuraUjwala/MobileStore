from django.db import models
from django.contrib.auth.models import User


class Brand(models.Model):
    name=models.CharField(max_length=100, unique=True)
    logo=models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name
    
class lapBrand(models.Model):
    name=models.CharField(max_length=100, unique=True)
    logo=models.ImageField(upload_to='brand_logos/')

    def __str__(self):
        return self.name

class mobiles(models.Model):
    image=models.ImageField(upload_to='mobiles/')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    origprice=models.IntegerField(null=True)  # Make this nullable
    ram=models.CharField(max_length=30, null=True)
    rom=models.CharField(max_length=30, null=True)
    camera=models.CharField(max_length=100, null=True)
    battery=models.CharField(max_length=100, null=True)
    overview=models.TextField(max_length=3000, null=True)
    is_bestselling=models.BooleanField(null=True, default=False)
    is_deals=models.BooleanField(null=True, default=False)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE, null=True, blank=True)  # Ensure this links to Brand
    
    # Optional: Adding additional fields for discount, EMI, and delivery date
    discount=models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    emi_price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_date=models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Slides(models.Model):
    img=models.ImageField(upload_to='media/')

class Offer(models.Model):
    off=models.IntegerField()
    img=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=50)
    off_price=models.IntegerField()
    old_price=models.IntegerField()

class laptops(models.Model):
    image=models.ImageField(upload_to='media/')
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    origprice=models.IntegerField(null=True)  # Make this nullable
    display=models.CharField(max_length=100, null=True)
    memory=models.CharField(max_length=100, null=True)
    processor=models.CharField(max_length=100,null=True)
    os=models.CharField(max_length=100,null=True)
    overview=models.TextField(max_length=3000, null=True)
    is_bestselling=models.BooleanField(null=True, default=False)
    is_deals=models.BooleanField(null=True, default=False)
    brand=models.ForeignKey(lapBrand, on_delete=models.CASCADE, null=True, blank=True)  # Ensure this links to Brand
    discount=models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    emi_price=models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    delivery_date=models.DateField(null=True, blank=True)

class Accessories(models.Model):
    image = models.ImageField(upload_to='accessories/')
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Newly_lanched=models.BooleanField(null=True, default=False)
    orginalprice=models.DecimalField(max_digits=10, decimal_places=2)
    Brand=models.CharField(max_length=20,null=True,)
    warrenty=models.IntegerField(null=True,)
    lanch_year=models.IntegerField(null=True,)

    def __str__(self):
        return self.name







