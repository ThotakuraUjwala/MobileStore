from django.shortcuts import render
from .models import *

def home(request):
    slidesdata = Slides.objects.all()
    bestselling = mobiles.objects.filter(is_bestselling=True)
    brands = Brand.objects.all()
    offerdata=Offer.objects.all()
    bestlap=laptops.objects.filter(is_bestselling=True)
    lapoff=laptops.objects.filter(is_deals=True)
    return render(request, 'home.html', {'slidesdata': slidesdata, 'bestselling': bestselling, 'brands': brands,'bestlap':bestlap,'lapoff':lapoff,'moboff':offerdata})

def brand_view(request, brand_name):
    brand = Brand.objects.get(name__iexact=brand_name)
    mobiles_by_brand = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'mobiles': mobiles_by_brand, 'brand': brand})

def mobiledataview(request, id):
    mobiledata = [mobiles.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})


def lapdataview(request, id):
    lapdata = [mobiles.objects.get(id=id)]
    return render(request, 'lapdata.html', {'lapdata': lapdata})

def allmobiles(request):
    data = mobiles.objects.all()
    return render(request, 'allmobiles.html', {'alldata': data})

def cart(request):
    cartnum=mobiles.objects.all()
    return render(request, 'cart.html', {'cartnum': cartnum})

def brand_mobiles_view(request, brand_name):
    brand = Brand.objects.get(name=brand_name)  # Assuming you have a Brand model
    mobiles_list = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'brand': brand, 'mobiles': mobiles_list})

def offer(request):
    offerdata=Offer.objects.all()
    return render(request,'home.html',{'offerdata':offerdata})

