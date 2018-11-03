from django.db import models

# Create your models here.

class Monitoria(models.Model):
    mentor = models.CharField(max_length=50, blank=True) #ID usuario #alterar para foreign key da model usuario
    nome = models.CharField(max_length=50, blank=True)
    conteudo = models.CharField(max_length=200, blank=True)
    imagem = models.CharField(max_length=100, blank=True)
    dataHora = models.CharField(max_length=100, null=True)
    tag = models.CharField(max_length=30, blank=True)
