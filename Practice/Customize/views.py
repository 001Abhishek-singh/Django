from django.shortcuts import render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def mycustomsignin(request):
    if request.method == 'POST':
        username = request.POST.get('Username')
        useremail = request.POST.get('Email')
        # userphone = request.POST.get('Number')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 == password2:
            my_user = User.objects.create_user(username,useremail,password1)
            my_user.save()
            return HttpResponse("Data saved successfully!!!!")
        
    return render(request,'customsignin.html',{})

def mycustomlogin(request):
    if request.method == 'POST':
        # myemail = request.POST.get('UserEmail')
        username = request.POST.get('Username')
        mypassword = request.POST.get('Loginpassword')

        user = authenticate(request,username=username,password=mypassword)
        if user is not None:
            login(request,user)
            return render(request,'newhome.html',{})
        else:
            return HttpResponse("Bad Credentials!!!!")
    return render(request,'customlogin.html',{})

def mylogout(request):
    logout(request)
    return HttpResponse("Mai to logout ho gya")

@login_required(login_url='custom/home') # it is a decorator which is used to protect the url from any other user or from the attacker.
def newhome(request):
    return render(request,'newhome.html',{})
