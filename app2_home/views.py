from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def mainwindow(Request):
    return HttpResponse("<h3><a href='http://127.0.0.1:8000/app1_home'>Link to Register Page</a></h3>  <br> <h1> Link to Home Page </h1>")