from django.contrib import admin
from django.urls import path
from Shopkart.views import *

urlpatterns = [
    path('',home,name="home"),
    path('register/',register,name="register"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('new/',new,name="new"),
    path('register/login/',login,name="login"),
    path('user/',my_form,name='my_form_input'),
    path('check/',signup,name="signup")
    # path('registration/',registration,name="registration"),
]
