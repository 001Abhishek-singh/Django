from django.db import models

# Create your models here.

state_list = [
    ('Delhi','Delhi'),
    ('Bihar', 'Bihar'),
    ('Haryana', 'Haryana'),
    ('Rajasthan', 'Rajasthan'),
    ('Uttrakhand', 'Uttrakhand')
]


class resumeModel(models.Model):
    userName = models.CharField(max_length=150 , null=False)  # CharField recieve the value either string or number 
    userSurname = models.CharField(max_length=150 ,null=False)
    userContact = models.IntegerField(null=False)  # it will recieve only integer field
    userEmail = models.EmailField(null=False)    # it will recieve only email field
    DoB = models.DateField(auto_now=False,auto_now_add=False)  # here auto_now = False & auto_now_add = False indicate that the localhost or system cannot take the date automatically from the Setting
    locality = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    state = models.CharField(choices= state_list, max_length=150)  # choices only recieve either list or tuple
    pincode = models.PositiveIntegerField()   # positive value will be recieve by this pincode field
    profileImage = models.ImageField(upload_to = 'ProfileGallery', blank=True)    
    resumeHoleder = models.FileField(upload_to = 'ResumeFolder', blank=True)

