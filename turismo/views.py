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
		#mas ta dando erro
		
		return redirect('turismo/home.html')

	else:
		return render(request, 'turismo/hotel.html')

def busca_voo(request):
	if request.method == 'POST':
		voo1 = Voo()
		voo1.fields = procuraVoo.buscaVoos(request.POST.get('cidade_saida'), request.POST.get('pais_saida'),
			request.POST.get('cidade_entrada'), request.POST.get('pais_entrada'), 
			request.POST.get('data'))
		voo1.save()
		return redirect('turismo/home.html')

	else:
		return render(request, 'turismo/voo.html')

def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
			product = Product()
			product.title = request.POST['title']
			product.body = request.POST['body']
			if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
				product.url = request.POST['url']
			else:
				product.url = 'http://' + request.POST['url']
			product.icon = request.FILES['icon']
			product.image = request.FILES['image']
			product.pub_date = timezone.datetime.now()
			product.hunter = request.user
			product.save()
			return redirect('home')	

		else:
			return render(request, 'products/create.html', {'error': 'All fielsds are required.'})
	else:
		return render(request, 'products/create.html')
