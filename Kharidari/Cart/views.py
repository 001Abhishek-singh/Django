from django.shortcuts import render

# Create your views here.
def mycart(request):
    return render(request,'mycart.html',{})
