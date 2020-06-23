from django.shortcuts import render
from django.http import HttpResponse
from secondapp.forms import SignupForm
from secondapp.models import Signup

# Create your views here.
def signUp(request):
	if request.method=='POST':
		password=request.POST['lastName']+'@123'
		firstName=request.POST['firstName']
		lastName=request.POST['lastName']
		userName=request.POST['userName']
		mailId=request.POST['mailId']
		phoneNumber=request.POST['phoneNumber']
		age = request.POST['age']
		form = Signup(firstName=firstName,lastName=lastName,
			userName=userName,password=password,mailId=mailId,
			phoneNumber=phoneNumber,age=age)
		form.save()
		return HttpResponse('hi this is ur pwd'+password)
	form = SignupForm()
	return render(request,'secondapp/signup.html',{'form':form})

def signin(request):
	if request.method=='POST':
		uname=request.POST['uname']
		pwd=request.POST['pwd']
		rs = Signup.objects.all().filter(userName=uname,password=pwd)
		print(list(rs))
		if rs:
			return render(request,'secondapp/profile.html',{'rs':rs})
			#return HttpResponse('valid user')
		return HttpResponse('not valid')
	return render(request,'secondapp/login.html',{})



	