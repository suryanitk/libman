"""libman URL Configuration

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
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from library import views

urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('login/', views.login, name='login'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('loginsuccess/', views.login, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('addbook/', views.addbook, name='addbook'),
    path('viewbook/', views.viewbook, name='viewbook'),
    path('issuebook/', views.issuebook, name='issuebook'),
    path('returnbook/', views.returnbook, name='returnbook'),
    path('deletebook/', views.deletebook, name='deletebook'),
    path('issuedbook/', views.issuedbook, name='issuedbook'),
    path('viewstudent/', views.viewstudent, name='viewstudent'),
    path('viewfaculty/', views.viewfaculty, name='viewfaculty'),
]
