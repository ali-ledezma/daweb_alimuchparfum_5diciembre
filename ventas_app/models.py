from django.db import models

# Create your models here.
class Ventas(models.Model):
    id=models.IntegerField(primary_key=True)
    fecha_venta=models.DateField()
    cantidad=models.IntegerField(null=True, blank=True)
    total=models.IntegerField(null=True, blank=True)
    idsucursal=models.IntegerField(null=True, blank=True)
    idproducto=models.IntegerField(null=True, blank=True)
    idempleado = models.IntegerField(null=True, blank=True)
    idcliente=models.IntegerField(null=True, blank=True)


    def __str__(self) -> str:
        return self.fecha
