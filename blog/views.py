from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.
def main(request):
    posts = Post.objects.all
    return render(request, 'blog/main.html', {'posts_list' : posts})

def performance(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('performance',index)
    elif request.method == "GET":
        form = CommentForm()
        comments = Comment.objects.filter(post=post)
       # price = post.ticket_price
        return render(request, 'blog/performance.html', {'post':post, 'form':form, 'comments':comments, })

def new_performance(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.post_author = request.user
            post.save()
            return redirect('main')
    else:
        form = PostForm()
    
    return render(request, 'blog/new_performance.html', {'form': form})

def p_detail(request, index):
    post = get_object_or_404(Post, pk=index)
    return render(request, 'blog/p_detail.html', {'post':post})

def c_mypage(request):
    posts = Post.objects.all
    return render(request, 'accounts/c_mypage.html',{'posts_list' : posts})

def p_mypage(request):
    posts = Post.objects.all
    return render(request, 'accounts/p_mypage.html',{'posts_list' : posts})