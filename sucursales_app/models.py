from django.db import models

# Create your models here.
class Sucursal(models.Model):
    id=models.IntegerField(primary_key=True)
    direccion=models.CharField( max_length=30)
    telefono=models.CharField(max_length=10)
    correo=models.CharField(max_length=20)
    numero=models.IntegerField()
    nombre=models.CharField(max_length=15)
    cempleados=models.IntegerField()

    def __str__(self) -> str:
        return self.nombre
