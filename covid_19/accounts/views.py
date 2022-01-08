from django.shortcuts import render, reverse ,redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login ,logout
from .models import User
from .forms import regs
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

 
@login_required
def Profile(request):
    user = get_object_or_404(User, pk=request.user.pk)
    context = {'Profile': user,}
    return render(request, 'profile_user/profile.html', context)


#from profile_user.models import Profiles
# Create your views here.



#def signup(request):
  #  New_User = New_User.objects.create_user(
   #     username = request.POST.get('Reg_UserName_Input'),
   #     password = request.POST.get('Reg_Password_Input'),
   #     email    = request.POST.get('Email_Input'),
   # )
   # New_User.first_name = request.POST.get('FirstName_Input')
   # New_User.last_name = request.POST.get('LastName_Input')
   # New_User.set_password(request.POST.get('Reg_Password_Input'))
    #if you use User.objects.create you must user set_password() method.
    #New_User.set_password(request.POST.get('Password_Input'))
    #New_User.save()
    #return render(request, 'accounts/login.html')
    

            




def Login(requset):
    if requset.user.is_authenticated:
        return render(requset,'home/home.html')
    else:
        return render(requset, 'accounts/login.html')


def Loggin_in(requset):
    if requset.method == 'POST':
        Username = requset.POST.get('Log_UserName_Input')
        Password = requset.POST.get('Log_Password_Input')
        user_auth = authenticate(username=Username, password=Password)
        if user_auth is not None:
            login(requset, user_auth)
            return HttpResponseRedirect(reverse('home:home'))
        else:
            print('User   :', user_auth)
            return render(requset, 'accounts/login.html')

    else:
        return render(requset, 'accounts/login.html')



@login_required
def log_out(request):
	logout(request)
	return redirect('accounts:login')


def Sign_Up(requset):
    data = {}
    if requset.POST:
        print('request')
        form=regs(requset.POST or None)
        data["info"]=form
        if form.is_valid():
           print('valid')
           form.save()
           user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'],)
           login(requset,user)
           return render(requset,'home/home.html')
        else:
            print('form not vid')
        return render(requset, 'accounts/signup.html',data)
    
    else:
        print('not valid')
        data["info"] = regs()
        return render(requset, 'accounts/signup.html',data)




@login_required
def dashboard(requset):
    return render(requset, 'accounts/dashboard.html' ) 