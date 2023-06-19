from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.

class Blog(models.Model):
    blog_img = models.ImageField(blank=True, verbose_name='Blog Image', null=True, upload_to='uploads/')
    blog_title = models.CharField(max_length=100, verbose_name='Blog Title')
    blog_description = models.TextField(verbose_name='Description')
    blog_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name_plural = 'Blog'

    def __str__(self):
        return self.blog_title

    def img_url(self):
        if self.blog_img:
            return self.blog_img.url