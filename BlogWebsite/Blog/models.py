from django.db import models
from django.utils.html import format_html
# Create your models here.
title_list = [
    ('Wedding','Wedding'),
    ('Politics','Politics'),
    ('Climate','Climate'),
    ('Tourism','Toursim'),
    ('Employement','Employement'),
    ('History','History')
]
class BlogTitles(models.Model):
    Title = models.CharField(choices=title_list,max_length=250)
    def __str__(self) -> str:
        return self.Title

class Category(models.Model):
    Category_id = models.AutoField(primary_key=True)
    Writer_name = models.CharField(max_length=200,default=False)
    Category_title = models.ForeignKey(BlogTitles,on_delete=models.CASCADE,default=False)
    Description = models.TextField()
    Category_image = models.ImageField(upload_to='CategoryImage')
    Category_url = models.CharField(max_length=150)
    Category_date = models.DateTimeField(auto_now_add=True,null=True)

    # now we want to display our image on the main admin file as a profile image

    # def display(self):
    #     return format_html('<img src="/path/{dynamic image path}" />.format(self.image_field_name)')


    def DisplayImage(self):
       return format_html('<img src = "/Media/{}" style="width:30px; height:30px" />'.format(self.Category_image))


class Post(models.Model):
    Post_id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=350)
    Post_content = models.TextField()
    Post_url = models.CharField(max_length=200)
    Post_image = models.ImageField(upload_to='PostImage')
    Post_date = models.DateTimeField(auto_now_add=True,null=True)
    Post_category_link = models.ForeignKey(BlogTitles,on_delete=models.CASCADE)
    # how to use title field from Category model into the Post model inside the post_category_link field

    def DisplayImagePost(self):
        return format_html('<img src = "/Media/{}" style=" width: 30px ; height: 30px" />'.format(self.Post_image))