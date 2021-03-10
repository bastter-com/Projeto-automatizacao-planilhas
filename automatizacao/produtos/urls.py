from automatizacao.produtos.views import index
from django.urls import path


urlpatterns = [
    path("produtos/", index, name="index")
]
