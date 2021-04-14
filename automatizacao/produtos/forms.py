from django import forms
from automatizacao.produtos.models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ('cliente',)

    def save(self, user):
        instance = super().save(commit=False)
        instance.cliente = user
        instance.save()


class LoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput())
