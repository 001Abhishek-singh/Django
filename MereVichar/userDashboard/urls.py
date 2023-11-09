from userDashboard.views import userhomepage
from django.urls import path

urlspattern = [
    path('',userhomepage,name="userhomepage"),
]