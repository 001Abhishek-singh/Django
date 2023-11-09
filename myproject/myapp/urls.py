from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpattern = [
    path('admin/', admin.site.urls),
    path('create/',create),
    path('show/',show),
    path('/bank',media),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)