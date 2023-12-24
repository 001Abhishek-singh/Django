from django.shortcuts import render

# Create your views here.
def helper(request):
    return render(request,'helper.html',{})
