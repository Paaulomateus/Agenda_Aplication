from django.db import models
from django.utils import timezone

# Create your models here.

class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    nome = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.nome

class Contact(models.Model):
    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
        
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50, blank=True)
    telefone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    dataCadastro = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    imagem = models.ImageField(blank=True, upload_to='pictures/%Y/$m/')
    categiria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)

    

