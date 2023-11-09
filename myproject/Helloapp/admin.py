from django.contrib import admin
from .models import ForRegistration,Helloworld

# Register your models here.
class myregistration(admin.ModelAdmin):
    list_display = ('name','surname','fathername','mothername','email','course','department','phone','year','university','address','term')
    list_filter = ('name',)
    list_editable = ('phone',)
    search_fields = ('name',)


class forhello(admin.ModelAdmin):
    list_display = ('name','surname','aadhar','address','qualification','officer')

admin.site.register(ForRegistration,myregistration)
admin.site.register(Helloworld,forhello)   #Modelclass,Adminclass