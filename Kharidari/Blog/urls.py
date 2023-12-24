from Blog.views import userBlog
from django.urls import path

urlpatterns = [
    path('userBlog/',userBlog,name='userBlog'),
    # path('word/',word)
]

# This is a test comment