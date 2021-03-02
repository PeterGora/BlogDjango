from django.shortcuts import render
from django.http import HttpResponse
from models import Category, Post, Comment


def index(request):
    # lista opublikowanych wpisów posortowana od najnowszych do najstarszych
    return HttpResponse("Welcome to my  Blogoshpere!")

def login(request):
    pass

def logout(request):
    pass

def register(request):
    pass