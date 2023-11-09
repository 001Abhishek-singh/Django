# from django.shortcuts import render,HttpResponse
# from Emp_Manage_System.models import Role,Department,Employe
# from Emp_Manage_System.form import addEmp
# # Create your views here.

# # main function for the given project
# def homepage(request):
#     return render(request,"main.html",{})

# # creating function for viewing the Employee data
# def viewEmploye(request):
#     display = Employe.objects.all()
#     return render(request,"view.html",{'display':display})

# # creating function for adding the Employee data
# def addEmploye(request):
#     if(request.method == 'POST'):
#         form_obj = addEmp(request.POST,request.FILES)
#         # if form_obj.is_valid():
#         #     form_obj.save()

#         if form_obj.is_valid():
#             firstname = form_obj.cleaned_data['first_name']
#             lastname = form_obj.cleaned_data['last_name']
#             department = form_obj.cleaned_data['department']
#             bonus = form_obj.cleaned_data['bonus']
#             salary = form_obj.cleaned_data['salary']
#             role = form_obj.cleaned_data['role']
#             phone = form_obj.cleaned_data['phone']
#             hiredate = form_obj.cleaned_data['hire_date']
# # now we are going to create an object of the User Model
#             userValue = Employe(first_name = firstname, last_name = lastname , department = department, bonus = bonus, salary = salary, role = role, phone = phone, hire_date = hiredate)
#             userValue.save()

#         return HttpResponse("<h2>Your Data Saved Successfully....</h2>")
#     form_obj = addEmp()
#     obj = Employe.objects.all()
#     return render(request,"add.html",{'form':form_obj,'obj':obj})

# # creating function for the removal of Employee data
# def removeEmploye(request,id):
# #    if id:
# #     try:
# #         remove = Employe.objects.get(pk = id)
# #         remove.delete()
# #         return HttpResponse("Your Data Removed Successfully")
# #     except:
# #         return HttpResponse("Something Wrong....")

#     return render(request,"remove.html",{})

# # creating function for filtering the Employee data
# def filterEmploye(request):

#     if(request.method == 'POST'):
#         new_form = addEmp()
#     return render(request,"filter.html",{'new_form':new_form})
