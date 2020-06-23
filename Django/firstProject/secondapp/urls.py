from django.urls import path
from secondapp import views
urlpatterns=[
	path('signup/',views.signUp,name='signup'),
	path('signin/',views.signin,name='signin'),
	
]