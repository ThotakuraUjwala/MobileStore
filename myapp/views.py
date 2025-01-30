from django.shortcuts import render
from .models import Slides, bestselling

def home(request):
    slidesdata = Slides.objects.all()
    data = bestselling.objects.all()
    return render(request, 'home.html', {'slidesdata': slidesdata, 'data': data})

def mobiledataview(request, id):
    mobiledata = [bestselling.objects.get(id=id)]
    return render(request, 'mobiledata.html', {'mobiledata': mobiledata})

