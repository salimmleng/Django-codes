from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if  postForm.is_valid():
            postForm.instance.author = request.user
            postForm.save()
            return redirect('add_post')

    else:
        postForm = PostForm()

    return render(request,'add_post.html',{'form':  postForm})

@login_required
def edit_post(request,id):
    post = Post.objects.get(pk = id)
    postForm = PostForm(instance = post)
    if request.method == 'POST':
        postForm = PostForm(request.POST,instance = post)
        if  postForm.is_valid():
            postForm.instance.author = request.user
            postForm.save()
            return redirect('home')


    return render(request,'add_post.html',{'form':  postForm})

@login_required
def delete_post(request,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('home')