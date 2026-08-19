from django.db import models
from productos.models import Producto
from inventarios.models import Inventario

class Compras(models.Model):
    ESTATUS_CHOICES = [
        ('Procesada', 'Procesada'),
        ('Cancelada', 'Cancelada'),
    ]

    folio = models.CharField(max_length=50)
    fecha = models.DateField()
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    costo_compra = models.FloatField()
    subtotal = models.FloatField()
    iva = models.FloatField()
    total = models.FloatField()
    estatus = models.CharField(max_length=20, choices=ESTATUS_CHOICES, default='Procesada')

    def __str__(self):
        return f"{self.folio} - {self.producto.nombre} x {self.cantidad} ({self.estatus})"

    def save(self, *args, **kwargs):
        es_nueva = self.pk is None
        super().save(*args, **kwargs)
        if es_nueva and self.estatus == 'Procesada':
            self.inventario.cantidad += self.cantidad
            self.inventario.save()
            
