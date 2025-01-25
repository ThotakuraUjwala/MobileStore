from django.contrib import admin
from .models import *

# Register your models here.
class bestsellingAdmin(admin.ModelAdmin):
    list_display=['image','name','price','origprice']

admin.site.register(bestselling,bestsellingAdmin)