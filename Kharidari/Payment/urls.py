from Payment.views import OnlinePayment
from django.urls import path

urlpatterns = [
    path('onlinePayment/',OnlinePayment,name='OnlinePayment'),
]
