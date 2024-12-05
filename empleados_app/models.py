from django.db import models

# Create your models here.
class Empleado(models.Model):
    idempleados=models.IntegerField()
    nombre=models.CharField(max_length=50)
    telefono=models.IntegerField()
    salario=models.FloatField()
    curp=models.CharField(max_length=15)
    fecha_ingreso=models.DateField()
    idsucursal=models.IntegerField(null=True,blank=True)
    puesto=models.CharField(max_length=50)




    def __str__(self) -> str:
        return self.nombre
