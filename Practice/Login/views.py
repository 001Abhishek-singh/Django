from Login.models import Signup,Login
from django.shortcuts import render
from django.contrib import messages
# from django.contrib.auth import authenticate,login
# from django.contrib.auth.models import User
# value= User.objects.create_user("Rockstar","mailtoabhishek287@gmail.com","12341")
# value.save()
#from django.http import HttpResponse

# Create your views here.
def signin(request): # My Signin function
    #return HttpResponse("Hello user's")
    if request.method == 'POST':
        inp_name = request.POST.get('Username')
        inp_surname = request.POST.get('Usersurname')
        inp_email = request.POST.get('Email')
        inp_number = request.POST.get('Number')
        inp_password1 = request.POST.get('password1')
        inp_password2 = request.POST.get('password2')
        inp_options = request.POST.get('Options')
        inp_answer = request.POST.get('Answer')
        inp_image = request.POST.get('Image')

        if inp_password1 == inp_password2:
            user_value = Signup(inp_name,inp_surname,inp_email,inp_number,inp_password1,inp_password2,inp_options,inp_answer,inp_image)
            user_value.save()
            print(inp_options)
    return render(request,'Signup.html',{})

def userlogin(request): # My Login function
    if request.method == "POST":
        inp_login_useremail = request.POST.get('UserEmail')
        inp_login_password = request.POST.get('Loginpassword')
        # Creating the model object.
        Login_user = Login(inp_login_useremail,inp_login_password)
        messages.success(request,"data added successfully..")
        Login_user.save()

        # Trying to authenticate the user by using default login method.
        # creating authenticate class object.
        # user = authenticate(username = inp_login_useremail,password = inp_login_password)
        # if user is not None:
        #     login(request,user)
        #     return render(request,'userhome.html')
        # else:
        #     messages.error(request,"Credentials are not correct")
        #     return redirect('login.html')
        print(inp_login_useremail)
    return render(request,'login.html',{})

def userhome(request):
    return render(request,'userhome.html',{})



# def login(request):

#     if request.method =='POST':
#      username = request.POST.get('UserEmail')
#      password = request.POST.get('Loginpassword')

#      user = authenticate(request,Username = username,Password = password)
#      if user is not None:
#          login(request,user)
#          return redirect('userpage/')
#      else:
#          return HttpResponse("<h1>Credentials are not equal<h1>")
    #  my_user = authenticate(request,Usern=inp_login_useremail,Password=inp_login_password)
    #     if my_user is not None:
    #         login(request,my_user)
    #         print('hello user')
    #         return redirect('userpage/')
    #     else:
    #         messages.error(request,"Your credentials are not correct,Please re-check!!!!")
    #         return render(request,'login.html')