from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from automatizacao.produtos.models import Pedido, Produto
from automatizacao.produtos.forms import PedidoForm, LoginForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return redirect('success')
    form = PedidoForm()
    return render(request, "index.html", {"form": form})


@login_required
def success(request):
    return render(request, "success.html")


@login_required
def list_orders(request):
    pedidos = Pedido.objects.all()
    return render(request, "list_orders.html", {"pedidos": pedidos})


def create_users(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        username = request.POST['usuario']
        password = request.POST['senha']
        user = authenticate(username=username, password=password)
        if user is None:
            return HttpResponse('<h1> Erro! Usuário não encontrado!</h1>')
        login(request, user)
        return redirect('index')
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
