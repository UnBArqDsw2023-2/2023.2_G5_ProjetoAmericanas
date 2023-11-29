from django.shortcuts import render
from rest_framework import viewsets
from americanas.models.Usuario import Usuario

from americanas.serializers.UsuarioSerializer import UsuarioSerializar

# Create your views here.
class UsuarioViewSets(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    
    def get_queryset(self):
        return Usuario.objects.all()
    """ 
        ModelViewSet ele cria um crud de usuario automatico.
    """