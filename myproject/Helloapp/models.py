from django.db import models

# Create your models here.
# models means data which we manipulate for creating the dynamic template or web page.

class Helloworld(models.Model): # creating a class in the model.py file which is responsible for the management of the data.
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=150)
    aadhar = models.IntegerField()
    address = models.CharField(max_length=250)
    qualification = models.CharField(max_length=100)
    officer  = models.BooleanField(max_length=40)


class ForRegistration(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    fathername = models.CharField(max_length=200)
    mothername = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    course = models.CharField(max_length=140)
    department = models.CharField(max_length=140)
    year = models.IntegerField(max_length=340)
    university = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    term = models.BooleanField(default=True)
    
