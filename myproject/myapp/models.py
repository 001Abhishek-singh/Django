from django.db import models

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length = 150)
    course = models.CharField(max_length = 150)
    college = models.CharField(max_length = 140)
    roll = models.IntegerField(max_length = 50)
    condition = models.BooleanField(default = False)

    def __str__(self):
        return self.name
    

class Bank(models.Model):
    Bank_name = models.CharField(max_length= 200)
    Bank_state = models.CharField(max_length= 120)
    Bank_city = models.CharField(max_length = 120)
    Bank_address = models.CharField(max_length= 120)
    BanK_code = models.IntegerField(max_length=120)
    Bank_image = models.ImageField(upload_to='bank/')
    Bank_feedback = models.CharField(max_length= 400)
    Bank_reviews = models.IntegerField(max_length=1)

