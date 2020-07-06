from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Turismo

from . import hotel


class TurismoListView(ListView):
    model = Turismo
    template_name = 'turismo/home.html'

def busca_hotel(request):
	if request.method == 'POST':
		print(hotel.achaHotel(request.POST.get('cidade'), request.POST.get('adultos'),
			request.POST.get('noites'), request.POST.get('quartos'), request.POST.get('checkin'), 
			request.POST.get('pais') ))
		return redirect('turismo/home.html')

	else:
		return render(request, 'turismo/hotel.html')

def busca_voo(request):
	print()
	#if request.method == 'POST':
	#	if user is not None:
	#		return redirect('home')
	#	else:
	#		 return render(request, 'turismo/voo.html', {'error': 'username or password is incorrect.'})
	#else:
	#	return render(request, 'turismo/voo.html')
