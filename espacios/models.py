from django.db import models

class Espacio(models.Model):
    ESTADOS = (
        ('disponible', 'Disponible'),
        ('ocupado', 'Ocupado'),
        ('mantenimiento', 'Mantenimiento'),
    )

    numero = models.CharField(max_length=5, unique=True)
    nivel = models.IntegerField(default=1)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')

    def __str__(self):
        return f"Espacio {self.numero} (Nivel {self.nivel}) - {self.estado}"
