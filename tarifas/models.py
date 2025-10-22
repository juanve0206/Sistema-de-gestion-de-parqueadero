from django.db import models

class Tarifa(models.Model):
    TIPO_VEHICULO = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('bicicleta', 'Bicicleta'),
    )

    tipo_vehiculo = models.CharField(max_length=20, choices=TIPO_VEHICULO)
    valor_hora = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_vehiculo} - ${self.valor_hora}/hora"
