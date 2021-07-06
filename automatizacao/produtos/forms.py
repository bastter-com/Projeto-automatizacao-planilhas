from django import forms
from automatizacao.produtos.models import Pedido
from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


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
