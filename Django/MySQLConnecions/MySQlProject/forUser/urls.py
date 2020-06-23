from django.urls import path,include
from forUser import views
from django.contrib.auth import views as auth_views
urlpatterns=[
	path('home/',views.home,name='home'),
	path('signin/',views.signin,name='signin'),
	path('login/',auth_views.LoginView.as_view(template_name='forUser/login.html'),name='login'),
	path('logout/',auth_views.LogoutView.as_view(template_name='forUser/logout.html'),name='logout')
]