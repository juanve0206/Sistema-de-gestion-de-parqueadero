from django.contrib import admin
from .models import Espacio

@admin.register(Espacio)
class EspacioAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nivel', 'estado')
    list_filter = ('estado', 'nivel')
    search_fields = ('numero',)
    ordering = ('nivel', 'numero')
