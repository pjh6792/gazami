from django.shortcuts import render, redirect
from .models import Post

# Create your views here.
def main(request):
    posts = Post.objects.all
    return render(request, 'blog/main.html', {'posts_list' : posts})
