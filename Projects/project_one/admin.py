from django.contrib import admin
from project_one.models import ImageUploader

# Register your models here.
@admin.register(ImageUploader)
class imageSection(admin.ModelAdmin):
    list_display = ['id','Photos','Date']
