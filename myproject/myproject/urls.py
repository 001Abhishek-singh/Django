"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Helloapp.views import *

urlpatterns = [
    path("",home, name="home"),
    path('page2/',secondpage,name="secondpage"), # routing is performing.
    path('page5/',mytemplate,name="mytemplate"),# here we are just passing the function.
    path('page4/',formember,name="formember"),
    path('page3/',myindex,name="myindex"),
    path('kiska/',mykiska,name="mykiska"),
    path('sabka/',mysabka,name="mysabka"),
    path('tera/',mytera,name="mytera"),
    path('service/',include('Helloapp.urls')),
    path('admin/', admin.site.urls)
]
