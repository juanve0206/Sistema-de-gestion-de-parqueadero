from django.db import models
from vehiculos.models import Vehiculo
from espacios.models import Espacio
from tarifas.models import Tarifa

class SesionParqueo(models.Model):
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    tarifa = models.ForeignKey(Tarifa, on_delete=models.SET_NULL, null=True)
    hora_entrada = models.DateTimeField(auto_now_add=True)
    hora_salida = models.DateTimeField(blank=True, null=True)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.vehiculo.placa} - {self.espacio.numero}"

    def calcular_total(self):
        if self.hora_salida and self.hora_entrada and self.tarifa:
            horas = (self.hora_salida - self.hora_entrada).total_seconds() / 3600
            self.total_pagar = round(horas * float(self.tarifa.valor_hora), 2)
            return self.total_pagar
        return 0
