from django.shortcuts import render
from .models import *
# Create your views here.

def bestphones(request):
    data=bestselling.objects.all()
    return render(request,'bestselling.html',{'data':data})