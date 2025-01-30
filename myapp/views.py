from django.shortcuts import render
<<<<<<< HEAD
from .models import *
# Create your views here.
def slides(request):
    slidesdata=Slides.objects.all()
    return render(request,'home.html',{'slidesdata':slidesdata})
    
def bestphones(request):
    data=bestselling.objects.all()
    return render(request,'home.html',{'data':data})
=======
from .models import Slides, bestselling

def home(request):
    slidesdata = Slides.objects.all()
    data = bestselling.objects.all()
    return render(request, 'home.html', {'slidesdata': slidesdata, 'data': data})

def mobiledataview(request, id):
    mobiledata = [bestselling.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})
>>>>>>> a74f629798386e01c2c4e97b591e155474dcc487

