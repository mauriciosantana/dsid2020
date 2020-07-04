from django.shortcuts import render, redirect

#from .models import Product

def home(request):
	return render(request, 'turismo/home.html')
