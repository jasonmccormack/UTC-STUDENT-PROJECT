from django.shortcuts import render
from django.contrib.auth.models import User
from .models import AllMembers, ScrumTeam


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


def all_teams(request, *args, **kwargs):
    team = ScrumTeam.objects.all()
    context = {"teams" : team, }
    target_page = './html/all_teams.html'
    return render(request, target_page, context) 

def about(request, *args, **kwargs):
    target_page = './html/about.html'
    return render(request,  target_page ) 

def help(request, *args, **kwargs):
    target_page = './html/help.html'
    return render(request,  target_page )     

def contact(request, *args, **kwargs):
    target_page = './html/contact.html'
    return render(request,  target_page )        

""" 
def landingpage(request):
    return render(request, "./html/landingpage.html") """