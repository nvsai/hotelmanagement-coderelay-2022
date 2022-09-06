from django.shortcuts import render,redirect
from .models import Usertype,Complaint

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

def Viewcomplaints(request):
	if request.user.is_authenticated:
		muser=Usertype.objects.get(username=request.user.username)
		print(muser.usertype)
		if muser.usertype=='student':
			try:
				complaints=Complaint.objects.filter(person=request.user.username)
			except:
				complaints=[]
		else:
			complaints=Complaint.objects.all()
		eve={
			"event_d":complaints
			}
		return render(request,"allcomplaints.html",eve)
	return redirect('login')

def Home(request):
	if request.user.is_authenticated:
		if request.session['signup']:
			userx=Usertype()
			userx.username=request.user.username
			userx.usertype=request.session['usertype']
			userx.save()
			request.session['signup']=False
		if request.method=="POST":
			comp=Complaint()
			comp.hostel=request.POST.get('noh')
			comp.category=request.POST.get('category')
			comp.person=request.user.username
			comp.time=request.POST.get('picker')
			comp.room=request.POST.get('rn')
			comp.phone=request.POST.get('pn')
			comp.description=request.POST.get('description')
			comp.save()

		return render(request,'home.html')
	else:
		request.session['signup']=False
		return redirect('/login/')