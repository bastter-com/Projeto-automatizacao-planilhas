from django.contrib import admin
from django.urls import path, include
from automatizacao.produtos import urls as produto_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(produto_urls)),
]
