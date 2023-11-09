from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from .models import MyModel
from .forms import MyForm,SignUpForm



# Create your views here.
def home(request):
    return render(request,"home.html",{})
def register(request):
    return render(request,"registration.html",{})
def contact(request):
    return render(request,"contact.html",{})
def about(request):
    return render(request,"about.html",{})
def new(request):
    return render(request,"new.html",{})

def my_form(request):
    form = MyForm()
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your data saved successfully")
            return render(request,'checkaction.html',{'form':MyForm(request.GET)})
        else:
            form = MyForm()
    return render(request, 'checkaction.html', {'form': form})
 
def signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)

            # redirect user to home page
            return redirect('')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})














def login(request):

    # if request.method == "POST":
    #     print("data is saved")
    #     myname = request.POST.get("forname")
    #     mypassword1 = request.POST.get("forpassword1")
    #     mypassword2 = request.POST.get("forpassword2")

        # form = MyUserCreationForm()
        # myobj = Validation()
        # myobj.name = myname
        # myobj.password1 = mypassword1
        # myobj.password2 = mypassword2
        # form = MyUserCreationForm()
        # form.use_required_attribute = myname
        # form.password1 = mypassword1
        # form.password2 = mypassword2

        # form = MyUserCreationForm(request.POST)
        
        # form.save()
        # return HttpResponse("data saved")
        # print("data is coming")
        # return redirect("register/login/")
        # form = UserCreationForm(request.POST)
        # if form.is_valid():
        #     form.save()

        # myobj = Validation(request.POST)
        # myobj.save()
        # return HttpResponse("data saved")

    # data = {"form":form ,"name":"abhishek"}

    # return render(request,"login.html",{})

# def registration(request):
    return render(request,"registration.html",{})