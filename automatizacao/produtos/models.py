from django.db import models


class UnidadeMedida(models.Model):
    unidade_medida = models.CharField(unique=True, max_length=25)


class Produto(models.Model):
    catmat = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=100)
    descricao_detalhada = models.TextField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"CATMAT - {self.catmat} | Descrição: {self.descricao}"


class Pedido(models.Model):
    cliente = models.CharField(max_length=50)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField()

    def __str__(self):
        return f"Cliente: {self.cliente}. Produto: {self.produto}. Quantidade: {self.quantidade}."
