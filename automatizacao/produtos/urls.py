from automatizacao.produtos.views import index, success, list_orders, create_users, login_view, logout_view, create_workbook_view
from django.urls import path


urlpatterns = [
    path("", index, name="index"),
    path("sucesso/", success, name="success"),
    path("listar-pedidos/", list_orders, name="list_orders"),
    path("cadastro/", create_users, name="signup"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("create_workbook/", create_workbook_view, name="create_workbook"),
]
