from django.db import models

# Create your models here.
class Signup(models.Model):
    Name = models.CharField(max_length=150,)
    Surname = models.CharField(max_length=150)
    Email = models.EmailField(max_length=150,primary_key=True)
    Mobile_number = models.IntegerField()
    Password = models.CharField(max_length=150)
    Confirm_password = models.CharField(max_length=150)
    Emergency_options = models.IntegerField(default=None)
    Answer = models.CharField(max_length=350) # create a list of favourite questions so that in response their answer should be saved here.
    Image = models.ImageField(default=None)

class Login(models.Model):
    Username = models.EmailField(max_length=150,primary_key=True)
    Password = models.CharField(max_length=150)


  # Options = (
    #     (0,'Your favourite Pet name'),
    #     (1,'Your first School name'),
    #     (2,'Your favourite Teacher name'),
    #     (3,'Your favourite Subject'),
    #     (4,'Your best Friend name')
    # )