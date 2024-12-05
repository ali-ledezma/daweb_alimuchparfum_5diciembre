from django.db import models

# Create your models here.
class Producto(models.Model):
    idproducto=models.IntegerField(null=True)
    nombre=models.CharField(max_length=20)
    marca=models.CharField(max_length=20)
    stock=models.IntegerField()
    idproveedor=models.CharField(max_length=20)
    idsucursal=models.IntegerField()
    notas=models.TextField()


    def __str__(self) -> str:
        return self.nombre
