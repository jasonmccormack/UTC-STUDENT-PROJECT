"""TeamX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from django.http import HttpResponse, HttpResponseNotFound
from django.conf.urls import handler404, handler500
from django.contrib.auth import views
from django.core.mail import send_mail
from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from TeamXapp.views import (
    base,
    index,
    login,
    all_teams,
    about,
    help,
    contact,
    dashboard
)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login', login),
    path('admin/', admin.site.urls),
    path('', index),
    path('', base),
    path('all_teams/' , all_teams    , name ='all_teams'), 
    path('about/'     , about        , name ='about'), 
    path('help/'      , help         , name ='help'), 
    path('contact/'   , contact      , name ='contact'), 
    path('dashboard/' , dashboard    , name ='dashboard'), 
]

handler500 = 'TeamXapp.views.error_500'
handler404 = 'TeamXapp.views.error_404'
