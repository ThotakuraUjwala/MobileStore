from django.contrib import admin
from .models import *

class mobilesAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'price', 'origprice', 'is_bestselling', 'is_deals', 'brand']

class slidesAdmin(admin.ModelAdmin):
    list_display = ['img']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']

class lapBrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'logo']

class offerAdmin(admin.ModelAdmin):
    list_display=['off','img','name','off_price','old_price']

class laptopsAdmin(admin.ModelAdmin):
    list_display = ['image', 'name', 'price', 'origprice', 'is_bestselling', 'is_deals', 'brand']

class AccessoriesAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price','orginalprice','description']

admin.site.register(Accessories, AccessoriesAdmin)
admin.site.register(Offer,offerAdmin)
admin.site.register(Slides, slidesAdmin)
admin.site.register(mobiles, mobilesAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(laptops,laptopsAdmin)
admin.site.register(lapBrand, lapBrandAdmin)

