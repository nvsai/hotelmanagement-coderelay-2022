from django.db import models

# Create your models here.

class Usertype(models.Model):
	username=models.CharField(max_length=50,null=False,blank=False)
	usertype=models.CharField(max_length=20,null=False,blank=False)

class Complaint(models.Model):
	hostel=models.CharField(max_length=50,null=False,blank=False)
	category=models.CharField(max_length=50,null=False,blank=False)
	person=models.CharField(max_length=50,null=False,blank=False)
	time=models.CharField(max_length=50)
	room=models.CharField(max_length=50,null=False,blank=False)
	phone=models.CharField(max_length=50,null=False,blank=False)
	description=models.TextField()
