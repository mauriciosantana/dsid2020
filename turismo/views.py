from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Turismo


class TurismoListView(ListView):
    model = Turismo
    template_name = 'turismo/home.html'

def busca(request):
	if request.method == 'POST':
		if user is not None:
			return redirect('home')
		else:
			 return render(request, 'turismo/busca.html', {'error': 'username or password is incorrect.'})
	else:
		return render(request, 'turismo/busca.html')
