from django.shortcuts import render

# Create your views here.
def userBlog(request):
    return render(request,'userBlog.html',{})
