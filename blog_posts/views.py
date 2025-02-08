from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import Post, Comment
from django.contrib.auth.models import User
from django.core.paginator import Paginator

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(posts, 5)  # 每页显示5篇文章
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog_posts/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_posts/post_detail.html', {'post': post})

@login_required
def post_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        if title and content:
            post = Post.objects.create(
                title=title,
                content=content,
                author=request.user,
                image=image
            )
            post.publish()
            return redirect('post_detail', pk=post.pk)
    return render(request, 'blog_posts/post_edit.html')

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        return redirect('post_detail', pk=pk)
    if request.method == "POST":
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.save()
        return redirect('post_detail', pk=pk)
    return render(request, 'blog_posts/post_edit.html', {'post': post})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        text = request.POST.get('text')
        if text:
            Comment.objects.create(
                post=post,
                author=request.user,
                text=text
            )
    return redirect('post_detail', pk=pk)
