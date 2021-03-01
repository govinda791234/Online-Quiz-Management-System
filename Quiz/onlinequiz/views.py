from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm;
from django.http import HttpResponse
from .models import Questions

# Create your views here.
def index(request):
	return render(request,'index.html')

def login(request):
	if request.method=='POST':
		User_Name=request.POST['User_Name']
		Password=request.POST['Password']
		user=auth.authenticate(username=User_Name,password=Password)
		if user is not None:
			auth.login(request,user)
			return redirect('dashboard')
		else:
			messages.error(request,'Invalid Login Details')
			return redirect('login')

	else:
		return render(request,'login.html')

def register(request):
	if request.method=='POST':
		First_Name=request.POST['First_Name']
		Last_Name=request.POST['Last_Name']
		Email=request.POST['Email']
		User_Name=request.POST['User_Name']
		Password=request.POST['Password']
		Conf_Password=request.POST['Conf_Password']
		if Password==Conf_Password:
			if User.objects.filter(username=User_Name).exists():
				messages.error(request,'username Token')
				return redirect('register')
			elif User.objects.filter(email=Email).exists():
				messages.error(request,'Email already Exists')
				return redirect('register')
			else:
				user = User.objects.create_user(username=User_Name, password=Password, email=Email, first_name=First_Name, last_name=Last_Name)
				user.save();
				messages.success(request,'Account Created Successfully')
				return redirect('login')
		else:
			messages.error(request,'password And Confirm-Password Not Matching')
			return redirect('register')
	else:
		return render(request,'register.html')

def dashboard(request):
	total_question=Questions.objects.all().count()
	total_user=User.objects.all().count()
	return render(request,'dashboard.html',{'total_user':total_user,'total_question':total_question})
def logout(request):
	auth.logout(request)
	return redirect('login')
def manage_users(request):
	user=User.objects.all()
	return render(request,'manage_users.html',{'users':user})
def manage_questions(request):
	user=Questions.objects.all()
	return render (request,'manage_questions.html',{'users':user})

def delete_user(request,pk):
	User.objects.filter(id=pk).delete()
	messages.success(request,'Student Record Deleted Successfully')
	return redirect('manage_users')

def change_password(request):
	if request.method=='POST':
		form=PasswordChangeForm(request.user,request.POST)
		if form.is_valid():
			user=form.save()
			update_session_auth_hash(request, user) #importent
			messages.success(request, 'Your password was Successfully change')
			return redirect('login')
		else:
			messages.error(request, 'Please correct the error below')
	else:
		form=PasswordChangeForm(request.user)
		return render(request,'change_password.html',{'forms':form})

def add_question(request):
	if request.method=='POST':
		questions=request.POST['questions']
		choice1=request.POST['choice1']
		choice2=request.POST['choice2']
		choice3=request.POST['choice3']
		choice4=request.POST['choice4']
		currect_answer=request.POST['currect_answer']
		if Questions.objects.filter(questions=questions).exists():
			messages.error(request,'Questions allready exists')
			# return redirect('add_question')
			return render(request,'add_question.html')
		else:
			que_data=Questions(questions=questions,choice1=choice1,choice2=choice2,choice3=choice3,choice4=choice4,currect_answer=currect_answer)
			que_data.save();
			messages.success(request,'Questions Added Successfully')
			return render(request,'add_question.html')
	else:
		return render(request,'add_question.html')

def delete_question(request,pk):
	Questions.objects.filter(id=pk).delete()
	messages.success(request,'Questions Record Deleted Successfully')
	return redirect('manage_questions')

def Edit_questions(request,pk):
	question=Questions.objects.filter(id=pk).values()
	#messages.success(request,'Questions Record Updated Successfully')
	return render(request,'Edit_questions.html',{'qust':question})

def Update(request):
	if request.method == 'POST':
		quest_id=request.POST['question_id']
		quest=Questions.objects.get(id=quest_id)
		quest.questions=request.POST['questions']
		quest.choice1=request.POST['choice1']
		quest.choice2=request.POST['choice2']
		quest.choice3=request.POST['choice3']
		quest.choice4=request.POST['choice4']
		quest.currect_answer=request.POST['currect_answer']
		quest.save();
		messages.success(request,'Successfully Updated')
		return redirect('manage_questions')
	else:
		messages.error(request,'Not Updated')
		return redirect('manage_questions')


def edit_user(request,pk):
	user=User.objects.filter(id=pk).values()
	return render(request,'edit_user.html',{'users':user})
def update_user(request):
	if request.method == 'POST':
		userid=request.POST['user_id']
		up_user=User.objects.get(id=userid)
		user_password=request.POST['Password']
		user_conf_password=request.POST['Conf_Password']
		if user_password == user_conf_password:
			up_user.first_name=request.POST['First_Name']
			up_user.last_name=request.POST['Last_Name']
			up_user.email=request.POST['Email']
			up_user.username=request.POST['User_Name']
			up_user.password=request.POST['Password']
			up_user.save();
			messages.success(request,'User Details Updated Successfully')
			return redirect('manage_users')
		else:
			messages.error(request,'Password did not match')
			return redirect('edit_user')
	else:
		messages.error(redirect,'not updated')
		return redirect('edit_user')

def quiz(request):
	question=Questions.objects.all()
	count=Questions.objects.all().count()
	return render(request,'quiz.html',{'questions':question,'count':count})

'''def total_question(request):
	total_question=Questions.objects.filter().all().count()
	return render(request,'dashboard.html',{'total_question':total_question})

def total_user(request):
	total_user=User.objects.all().count()
	return render(request,'dashboard.html',{'total_user':total_user})'''
#def result(request):
	


	
