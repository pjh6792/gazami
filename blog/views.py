from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
# Create your views here.
def main(request):
    posts = Post.objects.all
    return render(request, 'blog/main.html', {'posts_list' : posts})

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

def c_mypage(request):
    return render(request, 'accounts/c_mypage.html')

def p_mypage(request):
    return render(request, 'accounts/p_mypage.html')