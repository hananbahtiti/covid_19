from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User
from .models import *

class regs(UserCreationForm):
	password1 = forms.CharField(label='Password', required=True, widget=forms.PasswordInput)

	password2 = forms.CharField(label='Confirm password', required=True, widget=forms.PasswordInput)


	class Meta:
		model = User 
		fields = ('first_name', 'last_name', 'email', 'password1', 'password2', 
	  'Phone_Number', 'Age', 'Country', 'Sickness', 'Gender', 'Smoking',)


