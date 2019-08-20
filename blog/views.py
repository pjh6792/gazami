from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Ticket
from .forms import PostForm, CommentForm, TicketForm
from accounts.models import CUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


#Import for search
from django.views.generic.edit import FormView
from .forms import SearchForm
from django.db.models import Q
from django.shortcuts import render

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
        tickets = Ticket.objects.filter(post=post)
        return render(request, 'blog/performance.html', {'post':post, 'form':form, 'comments':comments, 'tickets':tickets})

def pay(request, index):
    post = get_object_or_404(Post, pk=index)
    if request.method == 'POST':
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            ticket.post = post
            ticket.save()
            return redirect('performance', index)
    else:
        form = TicketForm()
    return render(request, 'blog/pay.html',{'form':form})


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
    tickets = Ticket.objects.all
    return render(request, 'blog/p_detail.html', {'post':post, 'tickets':tickets})

def c_mypage(request):
    posts = Post.objects.all
    tickets = Ticket.objects.all
    return render(request, 'accounts/c_mypage.html',{'posts_list' : posts, 'tickets_list' : tickets})

def p_mypage(request):
    posts = Post.objects.all
    return render(request, 'accounts/p_mypage.html',{'posts_list' : posts})

def post_like(request, index):
    post = get_object_or_404(Post, pk=index)

    if not request.user.is_active:
        return redirect('performance', username=post.author, url=post.url)

    user = User.objects.get(username = request.user)

    if post.likes.filter(id = user.id).exists():
        post.likes.remove(user)
    else :
        post.likes.add(user)
    return redirect('performance', username=post.post_author, url=post.url)

# def like(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if PostLike.objects.filter(post=post, user=request.user).count() == 0:
#         PostLike.objects.create(post=post, user=request.user)
#     return redirect('blog/performance', post_id=pk)