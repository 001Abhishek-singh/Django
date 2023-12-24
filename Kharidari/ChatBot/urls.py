from ChatBot.views import helper
from django.urls import path

urlpatterns = [
    path('helper/',helper,name='helper'),
]
