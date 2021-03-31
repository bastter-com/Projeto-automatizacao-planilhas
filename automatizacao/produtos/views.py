from django.shortcuts import render, redirect
from automatizacao.produtos.models import Pedido, Produto
from automatizacao.produtos.forms import PedidoForm


def index(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    form = PedidoForm()
    return render(request, "index.html", {"form": form})


def success(request):
    return render(request, "success.html")

def list_orders(request):
    pedidos = Pedido.objects.all()
    return render(request, "list_orders.html", {"pedidos": pedidos})
