from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import *


def home(request):
    slidesdata = Slides.objects.all()
    bestselling = mobiles.objects.filter(is_bestselling=True)
    brands = Brand.objects.all()
    offerdata=Offer.objects.all()
    bestlap=laptops.objects.filter(is_bestselling=True)
    lapoff=laptops.objects.filter(is_deals=True)
    lapbrands = lapBrand.objects.all()
    new_accessories = Accessories.objects.filter(Newly_lanched=True)
    return render(request, 'home.html', {'slidesdata': slidesdata, 'bestselling': bestselling, 'brands': brands,'bestlap':bestlap,'lapoff':lapoff,'moboff':offerdata,'lapbrands':lapbrands,'new_accessories': new_accessories })

def brand_view(request, brand_name):
    brand = Brand.objects.get(name__iexact=brand_name)
    mobiles_by_brand = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'mobiles': mobiles_by_brand, 'brand': brand})

def brand_mobiles_view(request, brand_name):
    brand = Brand.objects.get(name=brand_name)  # Assuming you have a Brand model
    mobiles_list = mobiles.objects.filter(brand=brand)
    return render(request, 'brand_mobiles.html', {'brand': brand, 'mobiles': mobiles_list})


def brand_laptops_view(request, brand_name):
    brand = get_object_or_404(lapBrand, name__iexact=brand_name)  # Case-insensitive search
    laptops_list = laptops.objects.filter(brand=brand)
    return render(request, 'brand_laptops.html', {'brand': brand, 'laptops': laptops_list})


def lapbrand_view(request, brand_name):
    brand = lapBrand.objects.get(name__iexact=brand_name)
    laptops_by_brand = laptops.objects.filter(brand=brand)
    return render(request, 'brand_laptops.html', {'laptops': laptops_by_brand, 'lapbrand': brand})

def mobiledataview(request, id):
    mobiledata = [mobiles.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})


def lapdataview(request, id):
    lapdata = [laptops.objects.get(id=id)]
    return render(request, 'lapdata.html', {'lapdata': lapdata})

def allmobiles(request):
    data = mobiles.objects.all()
    return render(request, 'allmobiles.html', {'alldata': data})

def all_laptops(request):
    data = laptops.objects.all()
    return render(request, 'laptops.html', {'alldata': data})

def cart(request):
    cartnum=mobiles.objects.all()
    return render(request, 'cart.html', {'cartnum': cartnum})

def accessories(request):
    accessories_data = Accessories.objects.all()  # Retrieve all accessories from the database
    return render(request, 'accessories.html', {'accessories_data': accessories_data})

from django.shortcuts import render, get_object_or_404
from .models import Accessories

def accessoriesview(request, id):
    accessoriesdata = [Accessories.objects.get(id=id)]
    return render(request, 'accessoriesdata.html', {'accessoriesdata': accessoriesdata})


def search(request):
    query = request.GET.get("q", "").strip()

    mobile= mobiles.objects.none()  # Instead of []
    accessorie = Accessories.objects.none()
    laptop = laptops.objects.none()

    if query:
        mobile = mobiles.objects.filter(name__icontains=query)
        accessorie = Accessories.objects.filter(name__icontains=query)
        laptop = laptops.objects.filter(name__icontains=query)

    return render(request, "search_results.html", {
        "query": query,
        "mobile": mobile,
        "accessorie": accessorie,
        "laptop": laptop,
    })








