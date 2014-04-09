from django.db import models

# Create your models here.
class Language(models.Model):
    language = models.CharField(max_length=255)
    code = models.CharField(max_length=5)

    def __unicode__(self):
        return self.language