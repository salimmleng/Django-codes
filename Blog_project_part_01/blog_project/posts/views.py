from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
# Create your views here.

def add_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if  postForm.is_valid():
            postForm.save()
            return redirect('add_post')

    else:
        postForm = PostForm()

    return render(request,'add_post.html',{'form':  postForm})


def edit_post(request,id):
    post = Post.objects.get(pk = id)
    postForm = PostForm(instance = post)
    if request.method == 'POST':
        postForm = PostForm(request.POST,instance = post)
        if  postForm.is_valid():
            postForm.save()
            return redirect('home')


    return render(request,'add_post.html',{'form':  postForm})


def delete_post(request,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('home')