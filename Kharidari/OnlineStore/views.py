from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'OnlineStore/index.html',{})
def cart(request):
    return render(request,'OnlineStore/cart.html',{})
def blogSide(request):
    return render(request,'OnlineStore/blog-single-sidebar.html',{})
def checkout(request):
    return render(request,'OnlineStore/checkout.html',{})
def contact(request):
    return render(request,'OnlineStore/contact.html',{})
def shopGrid(request):
    return render(request,'OnlineStore/shop-grid.html',{})
def product(request):
    return render(request,'OnlineStore/product.html',{})
def service(request):
    return render(request,'OnlineStore/service.html',{})
def shop(request):
    return render(request,'OnlineStore/shop.html',{})
def blog(request):
    return render(request,'OnlineStore/blog.html',{})
def page(request):
    return render(request,'OnlineStore/page.html',{})
