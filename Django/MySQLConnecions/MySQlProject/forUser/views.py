from django.shortcuts import render
from django.http import HttpResponse
#from django.contrib.auth.forms import UserCreationForm
from forUser.forms import UserSignInForm
# Create your views here.

def home(request):
	return render(request,'forUser/home.html',{})

def signin(request):
	if request.method=='POST':
		form = UserSignInForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse('done')
	form = UserSignInForm()
	return render(request,'forUser/signin.html',{'form':form})