from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView


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
        'title': ' BlogoSphere',
    }
    context_object_name = "posts"

    def get_queryset(self):
        return Post.objects.exclude(draft=True).order_by("-pub_date")


# def details(request,post_id):
#     post = Post.objects.get(id=post_id)
#     title = f'Post "{post.post_title}"'
#     context = {
#         'title': title,
#         'post': post,
#     }
#     return render(request, "blog/details.html", context)

class DetailsView(DetailView):
    template_name = "blog/post.html"
    extra_context = {
        'title': ' BlogoSphere',
    }
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        return Post.objects.exclude(draft=True).order_by("-pub_date")


class UserPostsView(LoginRequiredMixin, ListView):
    template_name = "blog/user_post.html"
    context_object_name = "posts"
    extra_context = {
        "title": "Review and edit your posts",
    }
    success_url = reverse_lazy("user-post")

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(created_by=user).order_by("-pub_date")


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = "blog/new_post.html"
    extra_context = {
        "title": "Add a new Post",
    }
    success_url = reverse_lazy("user-post")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostForm
    template_name = "blog/edit_post.html"
    success_url = reverse_lazy("user-post")
    context_object_name = "post"
    pk_url_kwarg = "post_id"

    def get_queryset(self):
        return Post.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = {
            "title": f"Edit:{self.object.title}"
        }
        context.update(kwargs)
        return super().get_context_data(**context)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CommentView(LoginRequiredMixin, CreateView):
    model = Comment
    template_name = "blog/comment.html"
    form_class = CommentForm

    success_url = reverse_lazy("index")

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['post_id']
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = {
              "title": "Add your comment",
            "post": Post.objects.get(id=self.kwargs['post_id'])
        }
        context.update(kwargs)
        return super().get_context_data(**context)
