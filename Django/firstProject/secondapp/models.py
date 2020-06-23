from django.db import models

# Create your models here.
class Signup(models.Model):

	firstName = models.CharField(max_length=50)
	lastName = models.CharField(max_length=50)
	userName = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	mailId = models.EmailField(null=True)
	phoneNumber = models.CharField(max_length=10)
	age=models.IntegerField(null=True)

	def __str__(self):
		return str(self.id)+' '+self.lastName