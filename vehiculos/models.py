from django.db import models
from usuarios.models import Usuario

class Vehiculo(models.Model):
    TIPO_VEHICULO = (
        ('carro', 'Carro'),
        ('moto', 'Moto'),
        ('bicicleta', 'Bicicleta'),
    )

    propietario = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'cliente'})
    placa = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_VEHICULO)
    color = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return f"{self.placa} - {self.marca} ({self.tipo})"
