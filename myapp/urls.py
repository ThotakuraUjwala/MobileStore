from django.urls import path
from .views import home, mobiledataview

app_name = 'myapp'

urlpatterns = [
    path('', home, name='home'),  # Use the combined home view for both slides and bestphones
    path('mobiledata/<int:id>', mobiledataview, name='mobiledata'),
]


