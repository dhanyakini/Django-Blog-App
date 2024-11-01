from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post, Comment
from django.utils import timezone
from blog.forms import PostForm, CommentForm

from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
##############################
################################
###################################
class AboutView(TemplateView):
    template_name = 'about.html'

class PostListView(ListView):
    model = Post
    template_name='blog/post_list_view.html'
    context_object_name = 'post_list'
    def get_queryset(self):
        return Post.objects.filter(published_time__lte=timezone.now()).order_by('-published_time')


class PostDetailView(DetailView):
    model = Post
    template_name='blog/post_detail_view.html'
    context_object_name = 'post_detail'

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail_view.html'
    template_name='blog/post_form.html'
    form_class = PostForm


    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail_view.html'
    template_name='blog/post_form.html'

    form_class = PostForm

    model = Post

class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=Post
    success_url=reverse_lazy('post_list')

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_draft.html'
    template_name='blog/post_draft.html'
    context_object_name = 'post_draft'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_time__isnull=True).order_by('created_time')

##############################
##############################
##############################
@login_required
def add_comment_to_post(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})

@login_required
def approveComment(request,pk):
    comment_=get_object_or_404(Comment,pk=pk)
    comment_.approve_comment();
    return redirect('post_detail',pk=comment_.post.pk)

@login_required
def deleteComment(request,pk):
    dcomment_=get_object_or_404(Comment,pk=pk)
    temp = dcomment_.post.pk
    dcomment_.delete()
    return redirect('post_detail', pk=temp)


@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)
