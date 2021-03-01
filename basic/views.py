from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from basic.models import Destination
def index(request):
	dests=Destination.objects.all()
	return render(request,'index.html',{'dests':dests})



