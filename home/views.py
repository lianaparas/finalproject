from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_view(request):
	return render(request, "homepage.html", {})

def info_view(request,): 
	return render(request, "info.html", {})

def menu_view(request,): 
	return render(request, "menu.html", {})

def topuser_view(request,): 
	return render(request, "topuser.html", {})