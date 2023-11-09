from ResumeUploader.models import resumeModel
from django.contrib import admin
# Register your models here.

@admin.register(resumeModel)
class resumeViewer(admin.ModelAdmin):
    list_display = ['userName','userSurname','userContact','userEmail','DoB','locality','city','state','pincode','resumeHoleder']
    list_filter = ['userName','userEmail','state']
    