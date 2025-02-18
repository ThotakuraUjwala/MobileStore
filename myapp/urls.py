from django.urls import path
from .views import *


app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),  
    path('mobiledata/<int:id>', mobiledataview, name='mobiledata'),
    path('mobiles/',allmobiles,name='allmobiles'),
    path('mobiles/<str:brand_name>/', brand_view, name='brand_mobiles'),
    path('mobiles/brand/<str:brand_name>/', brand_mobiles_view, name='brand_mobiles'),
    path('laptopdata/<int:id>', lapdataview, name='lapdata'),
    path('laptops/',all_laptops,name='all_laptops'),
    path('laptops/<str:brand_name>/', lapbrand_view, name='brand_laptops'),
    path('laptops/brand/<str:brand_name>/', brand_laptops_view, name='brand_laptops'),
    path('accessories/', accessories, name='accessories'),
    path('accessoriesdata/<int:id>', accessoriesview, name='accessoriesdata'),
    path("search-results/", search, name="search_results"),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('cart/', cart_page, name='cart_page'),
    path('add-to-cart/<str:category>/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<str:category>/<int:item_id>/',remove_from_cart, name='remove_from_cart'),
    path('place-order/<str:category>/<int:item_id>/',place_order, name='place_order'),
    path('checkout/', checkout, name='checkout'),
    path('owner', owner_orders, name='owner_orders'),
    path('order-success/',order_success, name='order_success'),
]


