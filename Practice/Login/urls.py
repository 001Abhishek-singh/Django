#from django.contrib import admin
from Login.views import signin,userhome,userlogin
from django.urls import path

urlpatterns = [
    #path('urls',function_name,name='something')
    path('',signin,name='signin'),
    path('login/',userlogin,name='userlogin'),
    path('userpage/',userhome,name='userhome'),
    # path('check/',login,name='check')
]