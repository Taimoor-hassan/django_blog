from django import urls
from django.http.response import HttpResponse
from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse
from .models import Category,Post
from django.db.models import Count

# Create your views here.

def errorhandler(request,exception):
    return render(request,'404.html')

def home(request):
    posts=Post.objects.all()
    categorys=Category.objects.all().annotate(posts_count=Count('post'))
    data={
        'post': posts,
        'category': categorys,
    }
    return render(request,'index.html',data)

def pdetail(request,url):
    post=Post.objects.get(url=url)
    categorys=Category.objects.all()
    data={
        'post': post,
        'category': categorys,
    }
    return render(request,'detail.html',data)

def cdetail(request,url):
    cat=Category.objects.get(url=url)
    categorys=Category.objects.all()
    post=Post.objects.filter(post_category=cat)
    data={
        'cat': cat,
        'category': categorys,
        'post': post,
    }
    return render(request,'cdetail.html',data)
    
def contact(request):
    categorys=Category.objects.all()
    data={
        'category': categorys,
    }
    return render(request,'contact.html',data)



    
