from django.shortcuts import render
from .models import *
# Create your views here.
def slides(request):
    slidesdata=Slides.objects.all()
    return render(request,'slides.html',{'slidesdata':slidesdata})
    
def bestphones(request):
    data=bestselling.objects.all()
    return render(request,'home.html',{'data':data})

def mobiledataview(request,id):
    mobiledata=[bestselling.objects.get(id=id)]
    return render(request,'mobiledata.html',{'mobiledata':mobiledata})
