from django.shortcuts import render,redirect
from .models import Usertype

# Create your views here.
from django.http import HttpResponse

def usertype(request):
	request.session['usertype']=request.POST.get('usertype')
	request.session['signup']=True
	return redirect('/signup/')

def back(request):
	del request.session['usertype']
	request.session['signup']=False
	return redirect('/signup/')

def Home(request):
	if request.user.is_authenticated:
		if request.session['signup']:
			userx=Usertype()
			userx.username=request.user.username
			userx.usertype=request.session['usertype']
			userx.save()
			request.session['signup']=False
		return render(request,'home.html')
	else:
		request.session['signup']=False
		return redirect('/login/')