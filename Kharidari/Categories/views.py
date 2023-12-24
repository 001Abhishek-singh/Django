from django.shortcuts import render

# Create your views here.
def items(request,slug):
    return render(request,'items.html',{})
