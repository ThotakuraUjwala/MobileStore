from django.urls import path
from .views import *

app_name='myapp'

urlpatterns=[
    path('',bestphones,name='bestsellingphone'),
    path('mobiledata/<int:id>',mobiledataview,name='mobiledata')
]

