from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post, Comment


def index(request):
    title = ' BlogoSphere'
    posts = Post.objects.order_by("-pub_date")
    context = {
        'title' : title,
        'posts' : posts,
    }
    return render(request, "blog/index.html", context)

def login(request):
    pass

def logout(request):
    pass

def details(request,post_id):
    post = Post.objects.get(id=post_id)
    title = f'Post "{post.post_title}"'
    context = {
        'title': title,
        'post' : post,
    }
    return render(request, "blog/details.html", context)