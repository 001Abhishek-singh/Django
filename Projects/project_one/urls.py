# from django.contrib import admin
from project_one.views import first_page
from django.urls import path

urlpatterns = [
    path('',first_page,name="myhomepage"),
]
