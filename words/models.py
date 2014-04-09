from django.db import models

from languages.models import Language
from typewords.models import TypeWord
# Create your models here.
class Word(models.Model):
    word = models.CharField(max_length=255)
    translate = models.ManyToManyField('self', related_name='translate_id', blank=True)
    synonym = models.ManyToManyField('self', related_name='synonym_id', blank=True)
    language = models.ForeignKey(Language, related_name='word_language_id')
    typeword = models.ForeignKey(TypeWord, related_name='typeword_id')

    def __unicode__(self):
        return self.word

from .signals import relate_words