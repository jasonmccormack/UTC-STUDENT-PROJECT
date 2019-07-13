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
    member_list = AllMembers.objects.all()
    logged_in = bool(randint(0,1))
    context = {'logged_in' : logged_in, 'member_list' : member_list}
    if logged_in:
        target_page = './html/index.html'
    elif not logged_in:
        target_page = './html/landingpage.html'

    return render(request, target_page, context)


""" 
def landingpage(request):
    return render(request, "./html/landingpage.html") """