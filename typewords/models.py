from django.db import models

from languages.models import Language
# Create your models here.
class TypeWord(models.Model):
    name = models.CharField(max_length=255)
    language = models.ForeignKey(Language, related_name='typeword_language_id')

    def __unicode__(self):
        return self.name