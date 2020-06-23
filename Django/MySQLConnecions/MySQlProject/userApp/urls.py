from django.urls import path
from userApp import views
from django.contrib.auth import views as auth_views
urlpatterns =[
	path('signUp/',views.signUp,name='signUp'),
	path('home/',views.home,name='home'),
	path('signin/',auth_views.LoginView.as_view(template_name='userApp/login.html'),name='login'),
	path('signout/',auth_views.LogoutView.as_view(template_name='userApp/logout.html'),name='logout'),
]