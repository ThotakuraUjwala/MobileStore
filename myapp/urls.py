from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),  # Use the combined home view for both slides and bestphones
    path('mobiledata/<int:id>', mobiledataview, name='mobiledata'),
    path('mobiles/',allmobiles,name='allmobiles'),
    path('cart/',cart,name='cart')
]


