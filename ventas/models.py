from django.db import models
from clientes.models import Cliente
from productos.models import Producto
from sucursales.models import Sucursal
from inventarios.models import Inventario

class Ventas(models.Model):
    ESTATUS_CHOICES = [
        ('Completada', 'Completada'),
        ('Cancelada', 'Cancelada'),
    ]

    folio = models.CharField(max_length=50)
    fecha = models.DateField(auto_now_add=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='mis_ventas')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.PROTECT, related_name='ventas_sucursal', null=True, blank=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE, null=True, blank=True)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='Completada')

    def __str__(self):
        return f"Venta {self.folio} - {self.cliente.nombre} ({self.estatus})"

    def save(self, *args, **kwargs):
        es_nueva = self.pk is None
        super().save(*args, **kwargs)
        if es_nueva and self.estatus == 'Completada' and self.inventario is not None:
            self.inventario.cantidad -= self.cantidad
            self.inventario.save()
            









    