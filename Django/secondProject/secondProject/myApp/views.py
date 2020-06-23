from django.shortcuts import render,redirect
from django.http import HttpResponse
from myApp.models import Emp

# Create your views here.
def signUp(request):
	if request.method=='POST':
		# here we will read data which is comming from user
		empid = request.POST['empid']
		empName =request.POST['empName']
		empDesig =request.POST['empDesig']
		salary  = request.POST['salary']

		obj = Emp(empid=empid,empName=empName,empDesig=empDesig,salary=salary)
		obj.save()
		return redirect('/showAll')
		#return HttpResponse('done')


	return render(request,'myApp/signup.html')

def showAll(request):
	data = Emp.objects.all()
	return render(request,'myApp/showAll.html',{'data':data})