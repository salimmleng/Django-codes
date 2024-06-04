from django.shortcuts import render
from posts.models import Post
from categories.models import Category

def home(request,category_slug =None):
    data = Post.objects.all()
    if category_slug is not None:
        category1 = Category.objects.get(slug = category_slug)
        data = Post.objects.filter(category = category1)

    categories = Category.objects.all()
    return render(request,'home.html',{'data':data, 'category': categories})
