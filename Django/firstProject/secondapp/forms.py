from django.forms import ModelForm
from secondapp.models import Signup

class SignupForm(ModelForm):
	class Meta:
		model = Signup
		fields = ['firstName','lastName','userName','mailId','phoneNumber','age']