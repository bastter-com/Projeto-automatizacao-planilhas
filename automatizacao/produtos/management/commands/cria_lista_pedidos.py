from django.core.management.base import BaseCommand

import xlsxwriter
from automatizacao.produtos.models import Pedido


def get_pedidos():  # sourcery skip: inline-immediately-returned-variable
    pedidos = Pedido.objects.all()
    return pedidos


def fill_dict_pedidos(pedidos):
    dados = {}
    for pedido in pedidos:
        dados.setdefault(pedido.cliente, []).append(pedido)

    return dados


def create_workbook():
    workbook = xlsxwriter.Workbook('pedidos.xlsx')
    pedidos = get_pedidos()
    dados = fill_dict_pedidos(pedidos)
    for cliente in dados:
        worksheet = workbook.add_worksheet(f"{cliente}")
        worksheet.write('A1', 'Produto')
        worksheet.write('B1', 'Quantidade')
        row = 1
        column = 0
        for pedido in dados[cliente]:
            worksheet.write(row, column, pedido.produto.descricao_detalhada)
            worksheet.write(row, column + 1, pedido.quantidade)
            row += 1
    workbook.close()


class Command(BaseCommand):
    help = "Cria planilha de pedidos dos clientes"

    def handle(self, *args, **kwargs):
        create_workbook()
        print("Planilha criada com sucesso!")