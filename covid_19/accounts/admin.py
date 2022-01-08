from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from .forms import *

class ManagingUsers(UserAdmin):

	add_form = regs

	list_display = ['email']
	search_fields = ['email']
	readonly_fields = ['date_joined', 'last_login']
	ordering = ('email',)

	filter_horizontal = []
	list_filter = []


	add_fieldsets = (

		('Add a new user', {
			'classes':('wide',),
			'fields': ('first_name', 'last_name','email', 'Age', 'password1', 'password2', 'is_admin', 'is_staff', 'is_active', 'is_superuser', 'Phone_Number', 'Country', 'Smoking', 'Gender', 'Sickness'),
			}),
		)
	
	fieldsets = (

		(None, {
			'fields': ('first_name', 'last_name',  'email', 'Age', 'password','is_admin', 'is_staff', 'is_active', 'is_superuser', 'date_joined','Phone_Number', 'Country', 'Smoking', 'Gender', 'Sickness')
			}),

		)
admin.site.register(User, ManagingUsers)