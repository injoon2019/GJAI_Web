from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello World!")

def login(request):
    return HttpResponse("Log in")

def signout(request):
    return HttpResponse("Sign out !")