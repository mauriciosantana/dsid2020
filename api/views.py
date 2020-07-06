from rest_framework import generics

from turismo.models import Turismo, Hotel, Voo
from .serializers import TurismoSerializer, HotelSerializer, VooSerializer


class TurismoAPIView(generics.ListAPIView):
    queryset = Turismo.objects.all()
    serializer_class = TurismoSerializer

class HotelAPIView(generics.ListAPIView):
	queryset = Hotel.objects.all()
	serializer_class = HotelSerializer

class VooAPIView(generics.ListAPIView):
	queryset = Voo.objects.all()
	serializer_class = VooSerializer
