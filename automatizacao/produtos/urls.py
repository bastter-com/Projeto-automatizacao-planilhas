from automatizacao.produtos.views import index, success, list_orders
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("sucesso/", success, name="success"),
    path("listar-pedidos/", list_orders, name="list_orders"),
]
