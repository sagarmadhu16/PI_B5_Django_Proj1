from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(Request):
#    return HttpResponse("<h1 style = 'background:pink'> Hello! all this is my first Django App </h1>")
    MY_DICT = {'insert_me': "I am Coming from view.py file of app1 Template"}
    return render (Request,'app1_home/Reg.html',context=MY_DICT)