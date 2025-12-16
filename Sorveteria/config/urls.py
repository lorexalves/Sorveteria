"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('clientes/', ClientesView.as_view(), name='clientes'),
    path('fornecedores/', FornecedoresView.as_view(), name='fornecedores'),
    path('sorvetes/', SorvetesView.as_view(), name='sorvetes'),
    path('sabores/', SaboresView.as_view(), name='sabores'),
    path('vendedores/', VendedoresView.as_view(), name='vendedores'),
    path('usuarios/', UsuariosView.as_view(), name='usuarios'),
    path('vendas/', VendasView.as_view(), name='vendas'),
    path('itens/', ItensVendaView.as_view(), name='itens'),
    path('pagamentos/', PagamentosView.as_view(), name='pagamentos'),
    path('parcelas/', ParcelasView.as_view(), name='parcelas'),
    path('estoque/', EstoqueView.as_view(), name='estoque'),
]

