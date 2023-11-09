from django.contrib import admin
from .models import Record,Bank
# Register your models here.

class search(admin.ModelAdmin):
    list_display = ('name','course','college','roll','condition',)
    # list_editable = ('course',)
    search_fields = ('name',)

class show(admin.ModelAdmin):
    list_display = ('Bank_name',)

admin.site.register(Record,search)
admin.site.register(Bank,show)