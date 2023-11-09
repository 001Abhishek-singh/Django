from django.contrib import admin
from .models import MyModel

#admin.site.register(MyModel)
@admin.register(MyModel)
class TakeValue(admin.ModelAdmin):
    list_display = ['fullname','surname','mobile_number']