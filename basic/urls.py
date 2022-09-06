from django.urls import path
#now import the views.py file into this code
from . import views 

urlpatterns=[
	path('usertype/',views.usertype),
	path('back/',views.back),
	path('',views.Home),
	path('viewcomplaints/',views.Viewcomplaints),
]