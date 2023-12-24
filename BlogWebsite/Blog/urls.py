from Blog.views import home,about,post,blog,read
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
# from django.contrib import admin
urlpatterns = [
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('post/',post,name='post'),
    path('blog/',blog,name='blog'),
    # path('readmore/<slug:url>/',read,name='readmore') # <slug:url> this will indicate the dynamic value after readmore url
    path('readmore/<int:id>',read,name='readmore')
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
