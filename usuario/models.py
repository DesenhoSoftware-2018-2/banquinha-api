from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

length = 5000

class Profile (models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key = True,
        related_name='user'
    )
    description = models.TextField(
        max_length = length,
        default = '',
        blank = True,
        null=True
    )
    achievement = models.TextField(
        max_length = length,
        default = '',
        blank = True,
        null=True
    )

    # event = models.ForeignKey(Event, on_delete=models.CASCADE)

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

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.user.save()
