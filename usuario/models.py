from django.db import models

name_length = 50
email_length = 150
senha_length = 10

class Usuario(models.Model):
    nome =  models.CharField(max_length = name_length, blank = True)
    email = models.CharField(max_length = email_length, blank = True)
    senha = models.CharField(max_length = senha_length, blank = True)

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
