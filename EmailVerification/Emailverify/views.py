from Emailverify.models import EmailVerify
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render,redirect
import uuid
from django.conf import settings
from django.core.mail import send_mail 
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
# Create your views here.

def Register(request):
    if request.method == 'POST': # here we are collecting all the data's which we have entered into the input field
        username = request.POST.get('username')
        email = request.POST.get('email') # collecting the email value from the email input field 
        password = request.POST.get('password')

    try:
        if User.objects.filter(username = username).first(): # here we are checking that the new user is already existed in the User model or not if yes then redirect to main register page
            messages.success(request,"username is already existing")
            return redirect('/') # if user already exist then redirect to main register page 
        if User.objects.filter(email = email).first():
            messages.success(request,"email is already existing") # by using the django messages function we are able to display our messages on the screen  
            return redirect('/')
        
        user_obj = User.objects.create(username = username,email = email) # here we are creating a new user who entered their name & email in the given respective fields
        user_obj.set_password(password) # storing the value of password into new user database
        user_obj.save() # here we are saving the data as well as password for the given user.

        auth_token = str(uuid.uuid4())
        profile_obj = EmailVerify.objects.create(user = user_obj,auth_token = auth_token) # str(uuid.uuid4()) ---> this will give the unique string token and here we are calling the uuid4() function.
         # here we are importing the uuid which provides a 'unique string' and we do this because we want to generate the unique token so that verification can be accomplished  
        # creating a new user profile by EmailVerify('modelname' which we have created in our models.py file).objects.create(new_user_object,token_value)
        profile_obj.save() # we are saving our new user data

        send_mail_after_registration(email,auth_token) # calling the send_mail_after_registration function and also passing the argument to the given function
        return redirect('/token') # as everything sets to go then we will redirect the page on '/token' site.
    except Exception as e:
        print(e)

    return render(request,'myregister.html',{})

def verify_email(request,auth_token): # creating a function to verify the registerd email
    try:
        profile_obj = EmailVerify.objects.filter(auth_token = auth_token).first() # in this line we are checking that the user is existing or not if existing then futher operations performed
        if profile_obj:  # here we are using the if condition if user is existing then only futher process occur
            if profile_obj.token_verified:
                messages.success(request,"Your account is already verified")
                return redirect('/login/')

            profile_obj.token_verified = True  # if user gets verified then token_verified value will be equal to True
            profile_obj.save()  # after verification the data gets saved
            messages.success(request,"Congrats! Your account has been verified") # printing the message on the success.html page
            return redirect('/login/') # redirecting the page onto the success.html after the completion of the verification process
        else:
            messages.success(request,"Something went Wrong!!")
            return redirect('/error/')  # if error occur then redirect to error.html page
    except Exception as e:
        print(e)

def send_mail_after_registration(email,token): # creating a function for email verification
    subject = 'Your accounts need to be verified' # email's subject
    message = f'Here is your link to verify your account http://127.0.0.1:8790/verify/{token}' # message for the respective email and their generated token value
    email_from = settings.EMAIL_HOST_USER  # sender email address
    recipient_list = [email]  # to whom we are sending the verification token code or value
    send_mail(subject,message,email_from,recipient_list) # argument for the send_mail function so that we can send the respective details to the user

@login_required(login_url='login/')
def mylogin(request):
    if request.method == 'POST':  # if request.method == POST then fetch the data from the input field
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user_login_obj = User.objects.filter(email = email).first() # in this line we are checking that username(user) is already existing or not
        if user_login_obj is None: # if user is not existing then display the given message and redirect to login page
            messages.success(request,'User not found')
            return redirect('/login/')

        profile_login_obj = EmailVerify.objects.filter(user = user_login_obj).first() # if user is existing in the database then this query will be run
        
        if not profile_login_obj.token_verified: # this line indicate that user is not verified then follow the below set of commands
            messages.success(request,'User is not verified,please check your email')
            return redirect('/login/')
    
        login_user = authenticate(email = email,password = password) # if user is present as well as user is verified then authentication process will be occur 
        if login_user is not None:  # if input credentials are wrong then below message will be display
            login(request,login_user) # this line follow the login procedure and as the user gets login it will redirect to success.html page
            # messages.success(request,'Congrats! login successfully')
            return redirect('/success/')
        else:
            messages.success(request,'wrong password')
            return redirect('/login/')
            
    return render(request,'mylogin.html',{})

def forgetPassword(request):
    return render(request,'forgetPassword.html',{})

def success(request):
    return render(request,'success.html',{})

def token(request):
    return render(request,'token.html',{})

def error(request):
    return render(request,'error.html',{})
