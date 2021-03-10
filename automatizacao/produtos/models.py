from django.db import models


class UnidadeMedida(models.Model):
    unidade_medida = models.CharField(unique=True, max_length=25)


class Produto(models.Model):
    catmat = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=100)
    descricao_detalhada = models.TextField()
    unidade_medida = models.ForeignKey(UnidadeMedida, on_delete=models.SET_NULL, null=True)
