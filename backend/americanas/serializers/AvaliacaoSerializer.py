from rest_framework import serializers  
from americanas.models import Avaliacao


class AvaliacaoSerializers(serializers.ModelSerializer):
    titulo_avaliacao = serializers.CharField()
    nota = serializers.IntegerField()

    class Meta:
        model = Avaliacao
        fields = '__all__'