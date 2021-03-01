from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.
#from django.http import HttpResponse
def register(request):
	if request.method == 'POST' :
		first_name=request.POST['first_name']
		last_name=request.POST['last_name']
		username=request.POST['username']
		email=request.POST['email']
		password1=request.POST['password1']
		password2=request.POST['password2']
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.error(request,'username Token')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.error(request,'Email already Exists')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
				user.save();
				messages.success(request,'Account Created Successfully')
				return redirect('login')
		else:
			messages.error(request,'password And Confirm-Password Not Matching')
			return redirect('register')
	else:
		return render(request, 'register.html')

	#return render(request,'register.html')
def login(request):
	if request.method == 'POST':
		user_name=request.POST['user_name']
		password=request.POST['password']
		user=auth.authenticate(username=user_name, password=password)
		if user is not None:
			auth.login(request,user)
			return redirect('dashboard')
		else:
			messages.error(request,'Invalid Login Details')
			return redirect('login')
	else:
		return render(request,'login.html')


def dashboard(request):
	if request.session._session:
		return render(request,'dashboard.html')
	else:
		return render(request,'login.html')


def logout(request):
	
	auth.logout(request)
	return redirect('login')
