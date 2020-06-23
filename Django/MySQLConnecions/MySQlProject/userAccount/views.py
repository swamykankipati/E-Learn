from django.shortcuts import render
from django.http import HttpResponse
from userAccount.forms import UserRegisterForm
from userAccount.models import UserRegister
from django.core.mail import send_mail
from MySQlProject import settings
# Create your views here.

def upload(request):
	if request.method=='POST':
		form = UserRegisterForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			sub  = 'hi'
			body = 'i am comming from django app'
			receiver = request.POST['mailid']
			sender  = settings.EMAIL_HOST_USER
			send_mail(sub,body,sender,[receiver])
			return HttpResponse('Image uploaded.....')
	form  =UserRegisterForm()
	return render(request,'userAccount/upload.html',{'form':form})

def displayimages(request):
	data = UserRegister.objects.all()
	return render(request,'userAccount/displayimages.html',{'data':data})

def showAll(request):
	data = UserRegister.objects.all()
	return render(request,'userAccount/showAll.html',{'data':data})

def profile(request,id):
		data = UserRegister.objects.get(id = id)
		return render(request,'userAccount/profile.html',{'data':data})

