from django.shortcuts import render

# Create your views here.
# Create your views here.
def index(request):
    return render(request, "./html/index.html")

def base(request):
    return render(request, "/base.html")

def landingpage(request):
    return render(request, "./html/landingpage.html")