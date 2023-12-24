from django.shortcuts import render,redirect
from Blog.models import Post,Category
# Create your views here.
def home(request):
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})

def post(request):
    postObject = Post.objects.all()[0:11]
    data = {'postValue':postObject}
    return render(request,'post.html',data)

def blog(request):
    CategoryObj = Category.objects.all()
    return render(request,'blog.html',{'CategoryObj':CategoryObj})

def read(request,id):
    urlValue = Post.objects.get(pk = id)
    # data_display = resumeModel.objects.all()
    # return HttpResponse('candidate.html',{'id_picker':id_picker})
    return render(request,'read.html',{'urlValue':urlValue})
    # urlValue = Post.objects.get(Post_url = url) # single url value they will get and assign the url value into the url field
    # # data = {
    # #     "response": [urlValue.Post_id, urlValue.Title, urlValue.Post_content, urlValue.Post_image, urlValue.Post_url]
    # # }
    # # print(urlValue)
