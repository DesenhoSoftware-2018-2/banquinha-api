from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True)

class Evento(models.Model):
    nome = models.CharField(max_length=30, blank=True)
    data = models.DateTimeField(blank=True)
    imagem = models.CharField(max_length=30, blank=True)
    conteudo = models.CharField(max_length=30, blank=True)
    tag = models.ManyToManyField(Tag)

    class Meta:
        abstract = True

    @property
    def tag_FK(self):
        return self.tag.id

    def save( self, *args, **kwargs):
        super(Evento, self).save(*args, **kwargs)                
        tags_query_set = Tag.objects.all().values_list('id')        
        tags = [tag[0] for tag in tags_query_set]
        for tag in tags:
            self.tag.add(tag)
    
    def curtir(self):
        pass
        # implementacao do metodo curtir




class Monitoria(Evento):
    mentor = models.CharField(max_length=50, blank=True)

    # def clean(self, *args, **kwargs):
    #     if self.mentor.count() > 5:
    #         raise ValidationError("You can't assign more than three regions")
    #     super(Monitoria, self).clean(*args, **kwargs)
 