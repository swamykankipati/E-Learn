"""firstProject URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from firstApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hi/',views.hi,name='hai'),
    path('hello/<str:name>',views.hello,name='hello'),
    path('rollno/<int:id>',views.rollno,name='rollno'),
    path('message/',views.message,name='message'),
    path('register/',views.register,name='register'),
    path('details/',views.details,name='userDetils'),
    path('scboard/',views.scboard,name='scboard'),
    path('home/',views.home,name='home'),
    path('secondapp/',include('secondapp.urls')),



]
