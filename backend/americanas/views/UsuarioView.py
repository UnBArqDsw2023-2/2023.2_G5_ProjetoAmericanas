from django.shortcuts import render
from rest_framework import viewsets
from backend.americanas.models.Usuario import Usuario

from backend.americanas.serializers.UsuarioSerializer import UsuarioSerializar

# Create your views here.
class UsuarioView(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    get_queryset = Usuario.objects.all()
    