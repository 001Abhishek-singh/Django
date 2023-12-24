from ChatBot.views import home
from django.urls import path

# urlpatterns for ChatBot system
urlpatterns = [
    path('',home,name="home"),
]
