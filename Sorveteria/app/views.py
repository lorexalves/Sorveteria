from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from django.views import View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class ClientesView(View):
    def get(self, request, *args, **kwargs):
        clientes = Clientes.objects.all()
        return render(request, 'clientes/clientes.html', {
            'clientes': clientes
        })


class FornecedoresView(View):
    def get(self, request, *args, **kwargs):
        fornecedores = Fornecedor.objects.all()
        return render(request, 'fornecedores/fornecedores.html', {
            'fornecedores': fornecedores
        })


class SorvetesView(View):
    def get(self, request, *args, **kwargs):
        sorvetes = Sorvete.objects.all()
        return render(request, 'sorvetes/sorvetes.html', {
            'sorvetes': sorvetes
        })


class SaboresView(View):
    def get(self, request, *args, **kwargs):
        sabores = Sabor.objects.all()
        return render(request, 'sabores/sabores.html', {
            'sabores': sabores
        })


class VendedoresView(View):
    def get(self, request, *args, **kwargs):
        vendedores = Vendedor.objects.all()
        return render(request, 'vendedores/vendedores.html', {
            'vendedores': vendedores
        })


class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuarios.objects.all()
        return render(request, 'usuarios/usuarios.html', {
            'usuarios': usuarios
        })


class VendasView(View):
    def get(self, request, *args, **kwargs):
        vendas = Vendas.objects.all()
        return render(request, 'vendas/vendas.html', {
            'vendas': vendas
        })


class ItensVendaView(View):
    def get(self, request, *args, **kwargs):
        itens = ItensVenda.objects.all()
        return render(request, 'itens/itens.html', {
            'itens': itens
        })


class PagamentosView(View):
    def get(self, request, *args, **kwargs):
        pagamentos = Pagamento.objects.all()
        return render(request, 'pagamentos/pagamentos.html', {
            'pagamentos': pagamentos
        })


class ParcelasView(View):
    def get(self, request, *args, **kwargs):
        parcelas = Parcelas.objects.all()
        return render(request, 'parcelas/parcelas.html', {
            'parcelas': parcelas
        })


class EstoqueView(View):
    def get(self, request, *args, **kwargs):
        estoque = MovEstoque.objects.all()
        return render(request, 'estoque/estoque.html', {
            'estoque': estoque
        })
