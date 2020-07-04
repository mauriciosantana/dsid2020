from rest_framework import generics

from turismo.models import Turismo
from .serializers import TurismoSerializer


class TurismoAPIView(generics.ListAPIView):
    queryset = Turismo.objects.all()
    serializer_class = TurismoSerializer
