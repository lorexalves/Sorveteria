from django.contrib import admin
from .models import *

admin.site.register(Fornecedor)
admin.site.register(Sorvete)
admin.site.register(FornecedorSorvete)

admin.site.register(Sabor)
admin.site.register(SaborSorvete)

admin.site.register(Clientes)
admin.site.register(Vendedor)
admin.site.register(Usuarios)

admin.site.register(Vendas)
admin.site.register(ItensVenda)

admin.site.register(Pagamento)
admin.site.register(Parcelas)

admin.site.register(MovEstoque)
