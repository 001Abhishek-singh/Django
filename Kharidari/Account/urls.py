from Account.views import registration,userLogin
from django.urls import path

urlpatterns = [
    path('register/',registration,name='registration'),
    path('login/',userLogin,name='login'),
]

