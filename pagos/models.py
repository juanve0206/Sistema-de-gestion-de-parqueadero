from django.db import models
from sesiones.models import SesionParqueo

class Pago(models.Model):
    METODOS = (
        ('efectivo', 'Efectivo'),
        ('tarjeta', 'Tarjeta'),
        ('transferencia', 'Transferencia'),
    )

    sesion = models.OneToOneField(SesionParqueo, on_delete=models.CASCADE)
    metodo = models.CharField(max_length=20, choices=METODOS)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pago {self.id} - {self.sesion.vehiculo.placa}"
