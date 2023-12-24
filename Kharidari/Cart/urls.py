from Cart.views import mycart
from django.urls import path

urlpatterns = [
    path('addedItems',mycart,name='mycart'),
]
