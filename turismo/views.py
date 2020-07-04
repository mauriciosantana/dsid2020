from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Turismo


class TurismoListView(ListView):
    model = Turismo
    template_name = 'turismo/home.html'

def login(request):
	if request.method == 'POST':
		#user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
		if user is not None:
			#auth.login(request, user)
			return redirect('home')
		else:
			 return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
	else:
		return render(request, 'accounts/login.html')
