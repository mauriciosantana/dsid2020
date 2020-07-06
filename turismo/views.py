from django.shortcuts import render, redirect

from django.views.generic import ListView
from .models import Turismo

from . import hotel, procuraVoo


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

# como funciona isto

def busca_voo(request):

	if request.method == 'POST':
		print(procuraVoo.buscaVoos(request.POST.get('cidade_saida'), request.POST.get('pais_saida'),
			request.POST.get('cidade_entrada'), request.POST.get('pais_entrada'), 
			request.POST.get('data')))
# vai reiniciar		
		return redirect('turismo/home.html')

	else:
		return render(request, 'turismo/voo.html')
