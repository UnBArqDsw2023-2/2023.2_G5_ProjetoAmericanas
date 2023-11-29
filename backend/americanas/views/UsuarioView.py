from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from americanas.models.Usuario import Usuario

from americanas.serializers.UsuarioSerializer import UsuarioSerializar

# Create your views here.
class UsuarioViewSets(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializar
    queryset = Usuario.objects.all()
    
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = UsuarioSerializar(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

