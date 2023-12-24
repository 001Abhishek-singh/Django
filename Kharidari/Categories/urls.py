from Categories.views import items
from django.urls import path

urlpatterns = [
    path('Items/<slug>/',items,name='items'),
]
