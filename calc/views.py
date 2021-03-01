from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def home(request):
	return render(request,'home.html')
def add(request):
	val1=int(request.POST['first'])
	val2=int(request.POST['second'])
	res=val1+val2
	return render(request,'result.html',{'result':res})

