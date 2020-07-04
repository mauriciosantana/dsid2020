from rest_framework import generics

from turismo.models import Turismo
from .serializers import TurismoSerializer


class TurismoAPIView(generics.ListAPIView):

	# em vez de objects.all(), devemos criar uma funcao que retorna so as cidades procurada?
    queryset = Turismo.objects.all()
    serializer_class = TurismoSerializer
