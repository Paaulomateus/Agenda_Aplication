from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from . import models
from django.contrib.auth import password_validation

class ContactForms(forms.ModelForm):
    imagem = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept':'image/*',
            }
        ),
        required=False
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
    first_name = forms.CharField(
        required=True,
        min_length=3,
    )
    last_name = forms.CharField(
        required=True,
        min_length=3,
    )
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1','password2')
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            self.add_error(
                'email',
                ValidationError('Esse e-mail ja está sendo utilizado', code='invalid')
            )
        return email
    
class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatório.',
        error_messages={
            'min_length':'porfavor, adicione mais de 2 letras.'
        }
    )

    last_name = forms.CharField(
        min_length=2,
        max_length=30,
        required=True,
        help_text='Obrigatório.'
    )

    password1 = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete":"new-password"}),
        help_text=password_validation.password_validators_help_text_html(),
        required=False,
    )

    password2 = forms.CharField(
    label="Password 2",
    strip=False,
    widget=forms.PasswordInput(attrs={"autocomplete":"new-password"}),
    help_text='Use a mesma senha de antes',
    required=False,
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username')

    
    def save(self, commit = True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)

        password = cleaned_data.get('password1')

        if password:
            user.set_password(password)
        
        if commit:
            user.save()

        return user

    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 or password2:
            if password1 != password2:
                self.add_error(
                    'password2',
                    ValidationError('Senhas não correspondem')
                )

        return super().clean()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email

        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error(
                    'email',
                    ValidationError('Esse e-mail ja está sendo utilizado', code='invalid')
                )
        return email
    
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        if password1:
            try:
                password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error(
                    'password1',
                     ValidationError(errors)
                )

        return password1