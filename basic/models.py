from django.db import models

# Create your models here.

class Usertype(models.Model):
	username=models.CharField(max_length=50,null=False,blank=False)
	usertype=models.CharField(max_length=20,null=False,blank=False)
