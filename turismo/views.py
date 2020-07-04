from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Turismo


def home(request):
	return render(request, 'turismo/home.html')


class TurismoListView(ListView):
    model = Turismo
    template_name = 'home.html'
