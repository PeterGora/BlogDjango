from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post, Comment
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView
from django.views.generic.detail import SingleObjectMixin

# def index(request):
#     title = ' BlogoSphere'
#     posts = Post.objects.order_by("-pub_date")
#     context = {
#         'title' : title,
#         'posts' : posts,
#     }
#     return render(request, "blog/index.html", context)

class IndexView(ListView):
    template_name = "blog/index.html"
    extra_context = {
        'title' : ' BlogoSphere',
    }
    context_object_name = "posts"
    def get_queryset(self):
        return Post.objects.exclude(draft=True).order_by("-pub_date")

# class CreatePost(LoginRequiredMixin, CreateView):


def login(request):
    pass

def logout(request):
    pass

# def details(request,post_id):
#     post = Post.objects.get(id=post_id)
#     title = f'Post "{post.post_title}"'
#     context = {
#         'title': title,
#         'post': post,
#     }
#     return render(request, "blog/details.html", context)

class DetailsView(DetailView):
    template_name = "blog/details.html"
    extra_context = {
        'title': ' BlogoSphere',
    }
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        return Post.objects.exclude(draft=True).order_by("-pub_date")