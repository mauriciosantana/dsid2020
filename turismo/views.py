from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Turismo, Hotel, Voo
from . import hotel, procuraVoo

def base(request):
	return render(request, 'base.html')

def busca_hotel(request):
	if request.method == 'POST':
		hotel1 = Hotel()
		hotel1.fields = hotel.achaHotel(request.POST.get('cidade'), request.POST.get('adultos'),
			request.POST.get('noites'), request.POST.get('quartos'), request.POST.get('checkin'), 
			request.POST.get('pais'))
		hotel1.save()
		
		return render(request, 'base.html')

	else:
		return render(request, 'turismo/hotel.html')

def busca_voo(request):
	if request.method == 'POST':
		voo1 = Voo()
		voo1.fields = procuraVoo.buscaVoos(request.POST.get('cidade_saida'), request.POST.get('pais_saida'),
			request.POST.get('cidade_entrada'), request.POST.get('pais_entrada'), 
			request.POST.get('data'))
		voo1.save()
		return render(request,'base.html')

	else:
		return render(request, 'turismo/voo.html')
