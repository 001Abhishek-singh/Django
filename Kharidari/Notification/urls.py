from Notification.views import notification
from django.urls import path

urlpatterns = [
    path('notify/',notification,name='notification'),
]
