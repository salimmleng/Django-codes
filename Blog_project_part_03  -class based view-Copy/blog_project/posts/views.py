from django.shortcuts import render,redirect
from .forms import PostForm,CommentForm
from .models import Post
# required for class based view
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
# Create your views here.
@login_required
def add_post(request):
    if request.method == 'POST':
        postForm = PostForm(request.POST)
        if  postForm.is_valid():
            postForm.instance.author = request.user  # this line means which author is adding post
            postForm.save()
            return redirect('add_post')

    else:
        postForm = PostForm()

    return render(request,'add_post.html',{'form':  postForm})


# class based view add post
@method_decorator(login_required, name= 'dispatch' )
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('home')  # this line redirect to home page

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form) 




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


# class bassed edit post
@method_decorator(login_required, name= 'dispatch' )
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


@login_required
def delete_post(request,id):
    post = Post.objects.get(pk = id)
    post.delete()
    return redirect('home')


# class based delete view
@method_decorator(login_required, name= 'dispatch' )
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')


class DetailsPostView(DetailView):  # detail view app er singular name data guloke exess korai jehetu amer app eer name posts silo tai post singular name e access kora hoyse
    model = Post 
    pk_url_kwarg = 'id'
    template_name = 'post_details.html' 

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # post model er object store korlam
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form

        return context
    

        















