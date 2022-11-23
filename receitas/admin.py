from django.contrib import admin
from .models import Receita

class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'tempo_preparo', 'publicada')
    list_display_links = ('id', 'nome_receita')
# a virgula apos o 'nome_receita' identifica uma tupla
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
# Edição do campo da primeira tela do admin
    list_editable = ('publicada',)
    list_per_page = 5

admin.site.register(Receita, ListandoReceitas)