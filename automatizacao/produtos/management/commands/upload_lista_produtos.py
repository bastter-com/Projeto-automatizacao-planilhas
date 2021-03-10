from django.core.management.base import BaseCommand

import csv

from automatizacao.produtos.models import Produto

from time import time


class Command(BaseCommand):
    help = "Faz upload de lista de produtos"

    def handle(self, *args, **kwargs):
        with open("Produtos.csv", "r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";")
            start_time = time()
            produtos = []
            for row in reader:
                catmat, descricao = row["descricao"].split(' - ')
                descricao_detalhada = row["descricao detalhada"]
                unidade_medida = row["unidade de medida"]
                print(f"Lendo produto {descricao}")
                produto = Produto(
                    catmat=catmat,
                    descricao=descricao,
                    descricao_detalhada=descricao_detalhada,
                    unidade_medida=unidade_medida
                )
                produtos.append(produto)
            Produto.objects.bulk_create(produtos, ignore_conflicts=True)
            end_time = time()
            print(f"O programa demorou {end_time - start_time} segundos para inserir 330 linhas")
