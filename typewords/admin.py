from django.contrib import admin

# Register your models here.
from .models import TypeWord

class TypeWordAdmin(admin.ModelAdmin):
    list_display = ['name', 'language']
    list_filter = ['language']

admin.site.register(TypeWord, TypeWordAdmin)