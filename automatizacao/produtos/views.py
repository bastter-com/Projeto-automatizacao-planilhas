from django.shortcuts import render
from automatizacao.produtos.models import Produto


def index(request):
    produtos = Produto.objects.all()

    return render(request, 'index.html', {"produtos": produtos})
