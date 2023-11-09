# from django.contrib import admin
from ResumeUploader.views import homepage,candidateViewer
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',homepage,name='homepage'),
    path('candidate/<int:id>',candidateViewer,name="candidateViewer"),# url,function_name,functionurlname
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
