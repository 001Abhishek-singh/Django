# from django.shortcuts import render
# from ImageUploader.form import MyImageForm
# from ImageUploader.models import NewGallery

# # Create your views here.
# def home(request):
#     if(request.method == 'POST'):
#         form = MyImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#     form = MyImageForm()
#     display = NewGallery.objects.all()
#     return render(request,'index.html',{'form':form, 'display':display})
