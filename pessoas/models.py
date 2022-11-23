from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

# Codigo será referenciado para colocar o nome no combobox de receita
    def __str__(self):
        return self.nome
