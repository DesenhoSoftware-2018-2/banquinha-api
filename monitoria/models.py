from django.db import models
from django.db.models.signals import post_save
from django.core.exceptions import ValidationError
from usuario.models import Profile
# Create your models here.


class Tag(models.Model):
    tag = models.CharField(max_length=30, blank=True)

class Event(models.Model):
    name = models.CharField(max_length=30, blank=True)
    date = models.DateTimeField(blank=True)
    image = models.CharField(max_length=30, blank=True)
    content = models.CharField(max_length=30, blank=True)
    tag = models.ManyToManyField(Tag)
    mentored = models.ManyToManyField(Profile)

    class Meta:
        abstract = True

    @property
    def tag_FK(self):
        return self.tag.id

    def save( self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)                
        tags_query_set = Tag.objects.all().values_list('id')        
        tags = [tag[0] for tag in tags_query_set]
        for tag in tags:
            self.tag.add(tag)
    
    def like(self):
        pass
        # implementacao do metodo curtir
    
    def add_mentored(self, event_id, mentored_list):
        event = Event.objects.get(pk=event_id)
        for mentored in mentored_list:
            event.mentored.add(mentored)



class Monitoria(Event):

    def clean(self, *args, **kwargs):
        if self.mentor.count() > 4:
            raise ValidationError("Uma monitoria deve possuir no maximo 4 monitorados")
        super(Monitoria, self).clean(*args, **kwargs)
 