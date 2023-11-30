from rest_framework import serializers  
from americanas.models import Avaliacao


class AvaliacaoSerializer(serializers.ModelSerializer):
    titulo_avaliacao = serializers.CharField()
    comentario_avaliacao = serializers.CharField()
    nota = serializers.IntegerField()

    class Meta:
        model = Avaliacao
        fields = '__all__'