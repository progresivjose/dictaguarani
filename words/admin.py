from django.contrib import admin

from .models import Word
# Register your models here.

class WordAdmin(admin.ModelAdmin):
    filter_horizontal = ['translate', 'synonym']
    list_filter = ['language']
    list_display = ['word', 'language', 'typeword']
    search_fields = ['word']

admin.site.register(Word, WordAdmin)