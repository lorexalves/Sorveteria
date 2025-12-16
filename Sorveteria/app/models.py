
# Create your models here.
from django.db import models

# -----------------------------
# Fornecedor
# -----------------------------
class Fornecedor(models.Model):
    nome = models.CharField(max_length=45)
    telefone = models.CharField(max_length=15)
    cpf = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    instagram = models.CharField(max_length=45)
    site = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


# -----------------------------
# Sorvete / Produto
# -----------------------------
class Sorvete(models.Model):
    nome_produto = models.CharField(max_length=100)
    tipo_prod = models.CharField(max_length=2)
    descricao = models.CharField(max_length=200)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    custo = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    fabricacao = models.DateField(null=True, blank=True)

    fornecedores = models.ManyToManyField(
        Fornecedor,
        through='FornecedorSorvete'
    )

    def __str__(self):
        return self.nome_produto


# -----------------------------
# Tabela associativa Fornecedor x Sorvete
# -----------------------------
class FornecedorSorvete(models.Model):
    fornecedor = models.ForeignKey(Fornecedor, on_delete=models.CASCADE)
    sorvete = models.ForeignKey(Sorvete, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('fornecedor', 'sorvete')


# -----------------------------
# Sabor
# -----------------------------
class Sabor(models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)

    def __str__(self):
        return self.nome


# -----------------------------
# Tabela associativa Sabor x Sorvete
# -----------------------------
class SaborSorvete(models.Model):
    sabor = models.ForeignKey(Sabor, on_delete=models.CASCADE)
    sorvete = models.ForeignKey(Sorvete, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('sabor', 'sorvete')


# -----------------------------
# Clientes
# -----------------------------
class Clientes(models.Model):
    nome = models.CharField(max_length=45)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


# -----------------------------
# Vendedor
# -----------------------------
class Vendedor(models.Model):
    nome = models.CharField(max_length=80)
    cpf = models.CharField(max_length=15)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    conta_bancaria = models.CharField(max_length=45)
    salario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


# -----------------------------
# Usuários
# -----------------------------
class Usuarios(models.Model):
    login = models.CharField(max_length=45)
    senha = models.CharField(max_length=8)
    tipo_usuario = models.IntegerField()
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)

    def __str__(self):
        return self.login


# -----------------------------
# Vendas
# -----------------------------
class Vendas(models.Model):
    data_venda = models.DateField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pag = models.CharField(max_length=45)
    valor_final = models.DecimalField(max_digits=10, decimal_places=2)
    obs = models.CharField(max_length=45)
    desconto_item = models.DecimalField(max_digits=10, decimal_places=2)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)

    def __str__(self):
        return f"Venda {self.id}"


# -----------------------------
# Itens da Venda
# -----------------------------
class ItensVenda(models.Model):
    qtde = models.IntegerField()
    preco_venda = models.DecimalField(max_digits=10, decimal_places=2)
    preco_unit = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    sorvete = models.ForeignKey(Sorvete, on_delete=models.CASCADE)
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)


# -----------------------------
# Pagamento
# -----------------------------
class Pagamento(models.Model):
    tipo = models.CharField(max_length=45)
    valor_pag = models.DecimalField(max_digits=10, decimal_places=2)
    data_pag = models.DateField()
    venda = models.ForeignKey(Vendas, on_delete=models.CASCADE)


# -----------------------------
# Parcelas
# -----------------------------
class Parcelas(models.Model):
    qtd = models.IntegerField()
    valor_parc = models.DecimalField(max_digits=10, decimal_places=2)
    data_pag = models.DateField()
    data_venc = models.DateField()
    status_pag = models.CharField(max_length=45)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)


# -----------------------------
# Movimentação de Estoque
# -----------------------------
class MovEstoque(models.Model):
    qtd_estq = models.IntegerField()
    data_estoq = models.DateField()
    motivo = models.CharField(max_length=45)
    tipo_mov = models.CharField(max_length=45)
    sorvete = models.ForeignKey(Sorvete, on_delete=models.CASCADE)
