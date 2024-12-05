from django.db import models

# Create your models here.
class Proveedor(models.Model):
    idproveedor=models.IntegerField()
    nombre=models.CharField(max_length=100)
    rfc=models.CharField(max_length=15)
    telefono=models.IntegerField()
    direccion=models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.nombre
