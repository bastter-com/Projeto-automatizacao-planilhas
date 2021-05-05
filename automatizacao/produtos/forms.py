from django import forms
from automatizacao.produtos.models import Pedido
from django.forms import modelformset_factory


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ('cliente',)

    def save(self, user):
        instance = super().save(commit=False)
        instance.cliente = user
        instance.save()


PedidoFormSet = modelformset_factory(Pedido, exclude=('cliente',), extra=10)


class LoginForm(forms.Form):
    usuario = forms.CharField()
    senha = forms.CharField(widget=forms.PasswordInput())
