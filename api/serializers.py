from rest_framework import serializers

from turismo.models import Turismo


class TurismoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turismo
        fields = ('nome_cidade', 'date',)
