"""hardik URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
# from .views import view_name
from django.conf.urls import url, include 
from .views import home
from reddit_posts.views import show_posts, show_users

urlpatterns = [
    path('admin/', admin.site.urls),
    # path("abcd/", view_name , name = 'view_name'),
    url(r'^accounts/', include('allauth.urls')),
    # path('home/', admin.site.urls),
    path("home/", home , name = 'home'),

    path("show/", show_posts , name = 'show_posts'),

    path("show_users/", show_users , name = 'show_users'),






]
