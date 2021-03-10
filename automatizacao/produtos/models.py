from django.db import models


class Produto(models.Model):
    catmat = models.IntegerField(unique=True)
    descricao = models.CharField(max_length=100)
    descricao_detalhada = models.TextField()
    unidade_medida = models.CharField(max_length=25)
