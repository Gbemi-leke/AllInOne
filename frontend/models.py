from django.db import models
from django.contrib.auth import get_user_model
from users.models import *

# Create your models here.

class Blog(models.Model):
    blog_img = models.ImageField(blank=True, verbose_name='Blog Image', null=True, upload_to='uploads/')
    blog_title = models.CharField(max_length=100, verbose_name='Blog Title')
    blog_description = models.TextField(verbose_name='Description')
    blog_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.blog_title

    def img_url(self):
        if self.blog_img:
            return self.blog_img.url
        
class SubscribeModel(models.Model):
    email = models.EmailField(null=False, blank=True, max_length=200, unique=True)
    timestamp = models.DateTimeField( auto_now_add=True)

    def __str__(self):
        return self.email

class Contact(models.Model):
    subject = models.CharField(max_length=100)
    email= models.EmailField()
    first_name = models.CharField(max_length=100)
    message = models.TextField(max_length=200)
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    
    def __srf__(self):
        return self.first_name