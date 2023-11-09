from django.db import models

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length = 150)
    course = models.CharField(max_length = 150)
    college = models.CharField(max_length = 140)
    roll = models.IntegerField(max_length = 50)
    condition = models.BooleanField(default = False)

    def __str__(self) -> str:
        return self.name