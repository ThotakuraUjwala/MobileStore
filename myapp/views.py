from django.shortcuts import render
from .models import *

def home(request):
    slidesdata = Slides.objects.all()
    bestselling = mobiles.objects.filter(is_bestselling=True)
    return render(request, 'home.html', {'slidesdata': slidesdata, 'bestselling': bestselling})

def mobiledataview(request, id):
    mobiledata = [mobiles.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})


def allmobiles(request):
    data = mobiles.objects.all()
    return render(request, 'allmobiles.html', {'alldata': data})

def cart(request):
    cartnum=mobiles.objects.all()
    return render(request, 'cart.html', {'cartnum': cartnum})


