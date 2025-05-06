from django.contrib import admin
from contact import models

# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone','show')
    ordering = ('id',)
    search_fields = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    list_max_show_all = 200
    list_editable = ('nome', 'sobrenome','show')
    list_display_links = ('id', 'telefone')


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    ordering = ('-id',)
