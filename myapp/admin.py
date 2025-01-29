from django.contrib import admin
from .models import *

# Register your models here.
class bestsellingAdmin(admin.ModelAdmin):
    list_display=['image','name','price','origprice']
    
class slidesAdmin(admin.ModelAdmin):
    list_display=['img']

admin.site.register(Slides,slidesAdmin)
admin.site.register(bestselling,bestsellingAdmin)


# class mobiledataAdmin(admin.ModelAdmin):
#     list_display=['name','ram','rom','camera','battery','overview']
# admin.site.register(mobiledata,mobiledataAdmin)


