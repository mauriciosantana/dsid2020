from rest_framework import serializers

from turismo.models import Turismo, Hotel, Voo


class TurismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turismo
        fields = ('nome_cidade', 'date',)

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('fields',)

class VooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voo
        fields = ('fields',)
