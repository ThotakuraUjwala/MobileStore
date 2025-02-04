from django.contrib import admin
from .models import *

class mobilesAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'price', 'origprice', 'is_bestselling', 'is_deals', 'brand']

class slidesAdmin(admin.ModelAdmin):
    list_display = ['img']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']

class offerAdmin(admin.ModelAdmin):
    list_display=['off','img','name','off_price','old_price']

admin.site.register(Offer,offerAdmin)
admin.site.register(Slides, slidesAdmin)
admin.site.register(mobiles, mobilesAdmin)
admin.site.register(Brand, BrandAdmin)

