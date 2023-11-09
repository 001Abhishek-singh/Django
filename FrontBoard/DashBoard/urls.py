# from django.contrib import admin
from DashBoard.views import home
from django.urls import path

# urls list:
urlpatterns = [
    path('',home,name="home"),
]