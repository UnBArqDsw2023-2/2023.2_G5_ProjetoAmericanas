"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from americanas.views import UsuarioViewSets, PedidoViewSets, EnderecoViewSets,EnderecoUsuarioViewSets, ProdutoViewSets, AvaliacaoViewSets,AvaliacaoMetricasViewSets

router = routers.SimpleRouter()
router.register(r'usuario', UsuarioViewSets, basename='usuario')
router.register(r'pedido', PedidoViewSets, basename='pedido')
router.register(r'endereco', EnderecoViewSets, basename='endereco')
router.register(r'endereco_usuario', EnderecoUsuarioViewSets, basename='endereco_usuario')
router.register(r'produto', ProdutoViewSets, basename='produto')
router.register(r'avaliacao', AvaliacaoViewSets, basename='avaliacao')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('avaliacao_metricas/', AvaliacaoMetricasViewSets.as_view())
]
