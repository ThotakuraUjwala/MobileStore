from django.urls import path
from .views import *

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),  # Use the combined home view for both slides and bestphones
    path('mobiledata/<int:id>', mobiledataview, name='mobiledata'),
    path('mobiles/',allmobiles,name='allmobiles'),
    path('cart/', cart, name='cart'),
    path('mobiles/<str:brand_name>/', brand_view, name='brand_mobiles'),
    path('mobiles/brand/<str:brand_name>/', brand_mobiles_view, name='brand_mobiles'),
    path('laptopdata/<int:id>', lapdataview, name='lapdata'),
    path('laptops/',all_laptops,name='all_laptops'),
    path('laptops/<str:brand_name>/', lapbrand_view, name='brand_laptops'),
    path('laptops/brand/<str:brand_name>/', brand_laptops_view, name='brand_laptops'),
    path('accessories/', accessories, name='accessories'),



]


