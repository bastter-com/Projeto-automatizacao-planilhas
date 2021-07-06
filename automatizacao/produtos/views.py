from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from automatizacao.produtos.models import Pedido, Produto
from automatizacao.produtos.forms import LoginForm, PedidoFormSet, CustomUserCreationForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import EmailMessage
from automatizacao.produtos.management.commands.cria_lista_pedidos import create_workbook
from os import listdir, remove, path
from django.conf import settings


@login_required
def index(request):
    if request.method == "POST":
        formset = PedidoFormSet(request.POST)
        if formset.is_valid():
            instances = formset.save(commit=False)
            for instance in instances:
                instance.cliente = request.user
                instance.save()
            return redirect('success')
    formset = PedidoFormSet(queryset=Pedido.objects.filter(cliente=request.user))
    return render(request, "index.html", {"formset": formset})


@login_required
def success(request):
    return render(request, "success.html")


@login_required
def list_orders(request):
    pedidos = Pedido.objects.all()
    return render(request, "list_orders.html", {"pedidos": pedidos})


def create_users(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    form = CustomUserCreationForm()
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


@login_required
@user_passes_test(lambda user: user.is_superuser)
def create_workbook_view(request):
    create_workbook()
    file = [file for file in listdir('.') if file=="pedidos.xlsx"][0]
    filepath = path.join(settings.BASE_DIR, file)
    email = EmailMessage(
        "Planilha de pedidos", "Segue em anexo a planilha de pedidos requisitada no sistema.", settings.EMAIL_HOST_USER, [request.user.email]
    )
    email.attach_file(filepath)
    email.send()
    remove(filepath)
    return render(request, "create_workbook.html")
