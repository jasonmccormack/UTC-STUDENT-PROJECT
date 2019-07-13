from django.shortcuts import render
from .models import AllMembers
from random import randint

# Create your views here.
def base(request):
    return render(request, "/base.html")


def login(request):

    target_page = "./html/login.html"
    return render(request, target_page)


def index(request, *args, **kwargs):
    logged_in = bool(randint(0,1))
    if logged_in == True:
        target_page = './html/index.html'
    elif logged_in == False:
        target_page = './html/landingpage.html'

    return render(request, target_page)


""" 
def landingpage(request):
    return render(request, "./html/landingpage.html") """