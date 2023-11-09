'''from django.http import HttpResponse

def new(request):
    return HttpResponse("<p>HELLO   WORLD   NOW   I   AM   LEARNING   DJANGO </P>")'''

from django.http import HttpResponse
from django.shortcuts import render

def form(request):
    if request.method == 'post':
        print(request.post)
    return render(request,'firstform.html')

def newpage(request):
    if request.method == "POST":
        print(request.POST)
       
    Active = True
    Program = 'Django'
    Site = 'Youtube'
    platform = ['youtube','udemy','coursera','edx','coding ninja']
    mydic = {
        'movie': 'RRR',
        'anime': 'Pokemon',
        'sports': 'Football',
        'drink': 'Coffee',
        'color': 'Pink'
    }

    input = {
        'dicActive':Active,
        'dicProgram': Program,
        'dicSite' : Site,
        'dicPlatform': platform,
        'dicmydic' : mydic
    }
    return render(request,'myfile.html',input)



'''def home(request):
    return render(request,"index.html")

def page2(request):

    student_record = {
        'stu1':'Kunal',
        'stu2':'Vivek',
        'stu3':'shivam'
    }

    mylist = {'name': 'abhishek singh', # always need to prepare a dictionary for putting the data dynamically
    'class':'B.Tech',
    'Subject':'Software development',
    'Roll':'200202010049',
    'Personality':'Perfect',
    'student_data':student_record
    }
    return render(request,"page2.html",mylist) #This is a method use to put the "data dynamicall"

def page3(request):
    return render(request,"page3.html")

def loop(request):
    var = True
    i ={'name': 'abhishek',
        'roll no': '200202010049',
        'class': 'b.tech',
        'subject' : 'english'}
    store = {'myvalue':i,
             'myvariable':var}
    
    return render(request,'loop.html',store) '''

'''def index(request):
    return HttpResponse("<h1>LET'S SEE MY WEB PAGES</h1>")

def firstpage(request):
    return HttpResponse('hello world the competition in programming field is very high and due to which mostly student quite to learn the coding')

def secondpage(request):
    return HttpResponse("<h1> VIVEK IS MY BROTHER AND HE IS A GREAT PERSON</h1>")

def thirdpage(request):
    return HttpResponse("<p>world is so beautiful which i can't explain in simple words for that i need to express on the paper so that i looks good and energetic")'''
