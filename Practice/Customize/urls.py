#from django.contrib import admin
from django.urls import path
from .views import mycustomsignin,mycustomlogin,newhome,mylogout

urlpatterns = [
    #path('urls',function_name,name='something')
    path('page1/',mycustomsignin,name="mycustom"),
    path('page2/',mycustomlogin,name="mycustomlogin"),
    path('home/',newhome,name="newhome"),
    path('logout/',mylogout,name="mylogout")
]
