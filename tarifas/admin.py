from django.contrib import admin
from .models import Tarifa

@admin.register(Tarifa)
class TarifaAdmin(admin.ModelAdmin):
    list_display = ('tipo_vehiculo', 'valor_hora', 'descripcion')
    list_filter = ('tipo_vehiculo',)
    search_fields = ('tipo_vehiculo',)
    ordering = ('tipo_vehiculo',)
