from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trail_case(request):
    return render(request,'trail.html')
