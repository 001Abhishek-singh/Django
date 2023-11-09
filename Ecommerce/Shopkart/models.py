from django.db import models

from django.contrib.auth.models import User

users = User.objects.filter()

print(users[0].__dict__)

class MyModel(models.Model):
    fullname = models.CharField(max_length=200)
    surname = models.CharField(max_length=200,null=True)
    mobile_number = models.IntegerField()


