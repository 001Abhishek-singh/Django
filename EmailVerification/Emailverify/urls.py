from Emailverify.views import Register,mylogin,forgetPassword,success,token,error,verify_email
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Register,name="registration"),
    path('login/',mylogin,name="mylogin"),
    path('ForgetPassword/',forgetPassword,name="forgetPassword"),
    path('success/',success,name="success"),
    path('token/',token,name='token'),
    path('error/',error,name='error'),
    path('verify/<auth_token>/',verify_email,name='emailverification'), # passing the dynamic url so that verication can occur
]
