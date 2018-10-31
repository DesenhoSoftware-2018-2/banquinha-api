from django.db import models

# Create your models here.

class Monitoria(models.Model):
    nome = models.CharField(max_length=100, blank=True)
    conteudo = models.CharField(max_length=100, blank=True)
    imagem = models.CharField(max_length=100, blank=True)
    data = models.CharField(max_length=100, blank=True)
    hora = models.CharField(max_length=100, blank=True)
    tag = models.CharField(max_length=100, blank=True)
