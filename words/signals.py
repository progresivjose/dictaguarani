from django.db.models.signals import m2m_changed

def relate_words(sender, **kwargs):
    if(kwargs['action'] == 'post_add'):
        instance = kwargs['instance']
        #todos los sinonimos son traducciones de la traduccion
        if instance.synonym.exists():
            for translate in instance.translate.all():
                for synonym in instance.synonym.all():
                    translate.translate.add(synonym)
    pass

m2m_changed.connect(relate_words)