# from StudentData.forms import StudentRegistration
# from StudentData.models import User
# from django.shortcuts import render,HttpResponseRedirect

# # from django.http import HttpResponse

# # Create your views here.
# # def home(request):
# #     return HttpResponse("<h1>Hello world</h1>")

# # For Add Function
# def home(request):
#     if request.method == 'POST':
#         obj = StudentRegistration(request.POST)
#         # if obj.is_valid():
#         #     obj.save() // this method will be used to add the data into the model
#         if obj.is_valid():
#             in_name = obj.cleaned_data['name']
#             in_email = obj.cleaned_data['email']
#             in_password = obj.cleaned_data['password']
#             # now we are going to create an object of the User Model
#             userValue = User(name = in_name,email = in_email,password = in_password)
#             userValue.save()
#             obj = StudentRegistration()
#     else:
#         obj = StudentRegistration() 
#     data = User.objects.all()
#     return render(request,"add.html",{"form":obj,"display":data})


# # For Update Function
# def update_item(request,id):
#     if request.method == 'POST':
#         id_value = User.objects.get(pk=id)
#         obj2 = StudentRegistration(request.POST, instance = id_value)
#         if obj2.is_valid():
#             obj2.save()
#     else:
#         id_value = User.objects.get(pk=id)
#         obj2 = StudentRegistration(instance = id_value)
#     return render(request,"update.html", {"form_value": obj2})


# # For Delete Function
# def delete_item(request,id):
#     if request.method == 'POST':
#         remove = User.objects.get(pk = id) # Creating a variable where we store the command which we use for deleting the item
#         remove.delete()
#         return HttpResponseRedirect('/') # here we are redirecting the page at home      
    