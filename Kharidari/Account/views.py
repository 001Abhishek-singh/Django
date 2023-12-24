from django.shortcuts import render

# Create your views here.
def registration(request):
    return render(request,'Account/register.html',{})
def userLogin(request):
    return render(request,'Account/login.html',{})