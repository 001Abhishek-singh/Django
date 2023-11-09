from django.contrib import admin
from Login.models import Signup,Login

# Register your models here.
class Signup_User(admin.ModelAdmin):
    list_display = ['name','surname','email']
    list_filter = ['email']


class Login_user(admin.ModelAdmin):
    list_display = ['email']


admin.site.register(Signup)
admin.site.register(Login)


#@admin.register(Signup)
#@admin.register(Login)

