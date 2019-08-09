from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, Ticket
from .forms import PostForm, CommentForm, TicketForm
from accounts.models import CUser
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
        price = post.ticket_price
        tickets = Ticket.objects.filter(post=post)
        return render(request, 'blog/performance.html', {'post':post, 'form':form, 'comments':comments, 'price':price, 'tickets':tickets})

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



