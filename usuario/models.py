from django.db import models
from django.contrib.auth.models import User

length = 5000

class Usuario(models.Model):
    usuario = models.ForeignKey(
        User,
        related_name = 'User',
        null = True,
        on_delete = models.CASCADE
    )
    tokenUsuario = models.TextField(
        max_length = length,
        default = None,
        blank = True,
        null=True
    )
    # Campo que recebe a ForeignKey de avaliacao
    # Tirar da forma de comentario quando avaliacao já existir.
    # avaliacao = models.ForeignKey(
    #    'avaliacao.Avaliacao',
    #    on_delete=models.CASCADE,
    #    related_name='avaliacao',
    #)

    #@property
    #def avaliacaoFK(self):
    #    return self.avaliacao.id

    #implementar função da média da avaliação
