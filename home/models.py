from typing import Reversible
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils.html import format_html
from froala_editor.fields import FroalaField
from django.conf import settings
# from hitcount.models import HitCountMixin, HitCount


# Create your models here.

# model for catagory

class Category (models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    content= FroalaField(theme='dark')
    image=models.ImageField(upload_to='Category/')
    url=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True,null=True)
    def Image (self):
        return format_html('<img style="width:40px;height:40px;border-radius:50%" src="/media/{}"/>'.format(self.image))
    
    #to return string of object oyher tha its name 
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return Reversible('post-category', kwargs={'pk': self.pk})




#model for posts

class Post (models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=CASCADE)
    title=models.CharField(max_length=100)
    discription=models.CharField(max_length=100)
    content=FroalaField(theme='dark')
    image=models.ImageField(upload_to='Posts/')
    url=models.CharField(max_length=100)
    date=models.DateTimeField(auto_now_add=True,null=True)
    post_category=models.ForeignKey(Category, on_delete=CASCADE)
    def Image (self):
        return format_html('<img style="width:40px;height:40px;border-radius:50%" src="/media/{}"/>'.format(self.image))
    
    #to return string of object oyher tha its name 
    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return Reversible('post-detail', kwargs={'pk': self.pk})
