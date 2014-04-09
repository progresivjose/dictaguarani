from django.test import TestCase
from .models import Word
from languages.models import Language
from typewords.models import TypeWord
# Create your tests here.
class WordTest(TestCase):
    language = ""
    TypeWord = ""
    def setUp(self):
        self.language = Language.objects.create(language="Espanol", code="es")
        self.typeword = TypeWord.objects.create(name="Sustantivo", language=self.language)

    def test_related_synonim_signal(self):
        word = Word.objects.create(word="prueba", language=self.language, typeword=self.typeword)
        translate1 = Word.objects.create(word="traduccion", language=self.language, typeword=self.typeword)
        translate2 = Word.objects.create(word="traduccion2", language=self.language, typeword=self.typeword)
        synonym1 = Word.objects.create(word="sinonimo", language=self.language, typeword=self.typeword)
        synonym2 = Word.objects.create(word="sinonimo2", language=self.language, typeword=self.typeword)
        synonym3 = Word.objects.create(word="sinonimo3", language=self.language, typeword=self.typeword)

        word.translate.add(translate1)
        word.translate.add(translate2)
        word.synonym.add(synonym1)
        word.synonym.add(synonym2)
        word.synonym.add(synonym3)

        for t in translate2.translate.all():
            print t

