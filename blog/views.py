from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post, Comment


def index(request):
    # lista opublikowanych wpisów posortowana od najnowszych do najstarszych
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

def register(request):
    pass