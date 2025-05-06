from django import forms
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactForms(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        )
    )
    class Meta:
        model = models.Contact
        fields = (
            'nome', 'sobrenome', 'telefone',
            'email', 'descricao', 'categoria',
            'imagem',
        )
    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome')
        sobrenome = cleaned_data.get('sobrenome')

        if nome == sobrenome:
            mensagem = ValidationError('Nome ta igual ao sobrenome', code='invalid')
            self.add_error('nome', mensagem)
            self.add_error('sobrenome', mensagem)
        return super().clean()
    

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome == 'ABC':
            self.add_error('nome', ValidationError('veio do add error', code='invalid'))
        return nome

class RegisterForms(UserCreationForm):
    nome = forms.CharField(
        required=True,
        min_length=3,
    )
    sobrenome = forms.CharField(
        required=True,
        min_length=3,
    )
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','username','password1','password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Esse e-mail ja está sendo utilizado', code='invalid')
            )
        return email