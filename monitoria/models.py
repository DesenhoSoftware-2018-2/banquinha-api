from django.db import models

# Create your models here.

class Monitoria(models.Model):
    mentor = models.PositiveIntegerField(null=True) #ID usuario #alterar para foreign key da model usuario
    mentorado = models.PositiveIntegerField(null=True) #ID usuario #alterar para lista de ids da model ususario
    nome = models.CharField(max_length=50, blank=True)
    conteudo = models.CharField(max_length=200, blank=True)
    imagem = models.CharField(max_length=100, blank=True)
    dataHora = models.DateTimeField(null=True)
    tag = models.CharField(max_length=30, blank=True)
