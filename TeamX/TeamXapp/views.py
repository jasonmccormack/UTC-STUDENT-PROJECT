from django.shortcuts import render
from django.contrib.auth.models import User
from .models import AllMembers


# Create your views here.
def base(request):
    return render(request, "/base.html")


def login(request):
    target_page = "./registration/login.html"
    return render(request, target_page)


def index(request, *args, **kwargs):
    if User.is_authenticated:
        target_page = './html/index.html'
    elif not User.is_authenticated:
        target_page = './html/landingpage.html'

    return render(request, target_page)


""" 
def landingpage(request):
    return render(request, "./html/landingpage.html") """