from django.contrib import admin
from django.urls import path,include
from Helloapp.views import *

urlpatterns = [
    path('home/',myhome,name="myhome"),
    path('newhome/',mynewhome,name="mynewhome"),
    path('template/',fortemplate,name="fortemplate"),
    path('newtemplate/',newtemplate,name="newtemplate")
]