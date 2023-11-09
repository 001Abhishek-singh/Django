from django.db import models

# Create your models here.
class ImageUploader(models.Model):
    Photos = models.ImageField(upload_to="Gallery")
    Date = models.DateTimeField(auto_now_add=True)
    