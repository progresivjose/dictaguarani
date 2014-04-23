import json
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Word

# Create your views here.
def word_index(request):
    return render(request, 'word_index.html')

def word_view(request, word):
    #m_word = Word.objects.get(word=word)
    word = get_object_or_404(Word, word=word)

    """data = {
        'word' : m_word.word,
        'language' : m_word.language.language,
        'typeword' : m_word.typeword.name
    }"""

    #return render(request, 'word_view.html', {'word':data})
    return render(request, 'word_view.html', {'word':word})
