from Blog.models import Category,Post,BlogTitles
from django.contrib import admin

# Register your models here.
@admin.register(BlogTitles)
class BlogTitleAdmin(admin.ModelAdmin):
    list_display = ['Title']

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ['DisplayImage','Writer_name','Category_id','Category_title','Category_image','Category_date']
    list_filter = ['Writer_name','Category_id','Category_title']
    search_fields = ['Writer_name']
    list_per_page = 10

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ['DisplayImagePost','Title','Post_id','Post_date']
    class myMedia:
        jsFile = ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/sheet.js',)

