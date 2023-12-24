from django.shortcuts import render

# Create your views here.
def OnlinePayment(request):
    return render(request,'onlinePayment.html',{})
