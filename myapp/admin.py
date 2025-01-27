from django.contrib import admin
from .models import *

# Register your models here.
class bestsellingAdmin(admin.ModelAdmin):
    list_display=['image','name','price','origprice']

# class mobiledataAdmin(admin.ModelAdmin):
#     list_display=['name','ram','rom','camera','battery','overview']

admin.site.register(bestselling,bestsellingAdmin)
# admin.site.register(mobiledata,mobiledataAdmin)