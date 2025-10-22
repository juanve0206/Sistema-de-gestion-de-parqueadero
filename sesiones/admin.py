from django.contrib import admin
from .models import SesionParqueo

@admin.register(SesionParqueo)
class SesionParqueoAdmin(admin.ModelAdmin):
    list_display = ('vehiculo', 'espacio', 'tarifa', 'hora_entrada', 'hora_salida', 'total_pagar')
    list_filter = ('tarifa', 'espacio', 'vehiculo')
    search_fields = ('vehiculo__placa', 'espacio__numero')
    ordering = ('-hora_entrada',)
