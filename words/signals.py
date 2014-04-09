from django.db.models.signals import m2m_changed

def relate_words(sender, **kwargs):
    if(kwargs['action'] == 'post_add'):
        instance = kwargs['instance']
        #todos los sinonimos son traducciones de la traduccion
        if instance.synonym.exists():
            for translate in instance.translate.all():#recorre todas las traducciones de la palabra
                for synonym in instance.synonym.all():#recorre todos los sinonimos de la palabra
                    translate.translate.add(synonym) #asigna a los sinonimos como traducciones de la traduccion
    pass

m2m_changed.connect(relate_words)