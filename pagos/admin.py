from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('sesion', 'metodo', 'monto', 'fecha_pago')
    list_filter = ('metodo',)
    search_fields = ('sesion__vehiculo__placa',)
    ordering = ('-fecha_pago',)
