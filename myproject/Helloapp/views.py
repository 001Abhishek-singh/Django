from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import ForRegistration

# Create your views here.
# all the logical parts will be written inside this view page.
# there are two types of views (1) class based view (2)function based view

def home(request):
    return HttpResponse("Hello i am django lover")
    #return HttpResponse("<h1>Hello i am django lover...</h1>")
def secondpage(request):
    return HttpResponse("""<h1 style ="color:red">Hello budy it's just a trail for the work which we want to do in the custom field of the network and they are essential to play an important role everywhere and everytime.</h1>""")

def mytemplate(request):
    return render(request,"register.html",{})  # Note: here {} --- this represent for dynamic data.

def newtemplate(request):
    return render(request,"form.html",{})

def formember(request):
    return render(request,"mera.html") # creating a function where we check the html file work or not when present in member folder.

def myindex(request):
    return render(request,"index.html",{})

def mysabka(request):
    if request.method == 'POST':
        mypassword = request.POST['forpassword']
        myname = request.POST['forname']
        myemail = request.POST['foremail']
        print(mypassword)
        print(myname)
        print(myemail)

    data = {
        'myname': 'abhishek',
        'age': 21,
    }
    return render(request,"sabka.html",data) # here data is a dictionary where we can access the key value pair.

def mykiska(request):
    return render(request,"kiska.html",{})

def mytera(request):
    if request.method == 'POST':
        myinput = request.POST['textinput']
        print(myinput)
    isactive = 1 # 1 means true and 0 means false
    fromview = {
        'isactive':isactive,
        'university': 'IIT',
        'course': 'B.tech',
        'department': 'Electrical',
        'subject': 'control_system'      
    }
    return render(request,"tera.html",fromview)

def myhome(request):
    return HttpResponse("<h1>This is my Helloworld project where we will learn multiple things.</h1>")

def mynewhome(request):
    return HttpResponse("<p><h2>hello this side is lorem ispum jispum and many other things</h2></p>")

def fortemplate(request):

    if request.method == "POST":
        print("data is coming....")
        return redirect("/service/template")

    if request.method =="POST":
        # fetching the data
        myname = request.POST.get("Name")
        mysurname = request.POST.get("Surname")
        myfathername = request.POST.get("Father")
        mymothername = request.POST.get("Mother")
        myemail = request.POST.get("Email")
        myphone = request.POST.get("Phome")
        mycourse = request.POST.get("Course")
        mydepartment = request.POST.get("Dept.")
        myyear = request.POST.get("Year")
        myuniversity = request.POST.get("University")
        myaddress = request.POST.get("Address")
        myterm = request.POST.get("term&condition")

        # creating the model object
        obj = ForRegistration()

        obj.name = myname
        obj.surname = mysurname
        obj.fathername = myfathername 
        obj.mothername = mymothername
        obj.email = myemail
        obj.phone = myphone
        obj.course = mycourse
        obj.department = mydepartment
        obj.year = myyear
        obj.university = myuniversity
        obj.address = myaddress
        
        if myterm is None:
            obj.term = False
        else:
            obj.term = True

        # saving the data
        obj.save()

    return render(request,"template.html",{})