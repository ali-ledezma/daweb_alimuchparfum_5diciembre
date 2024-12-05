from django.db import models

# Create your models here.
class Cliente(models.Model):
    idcliente=models.IntegerField(null=True)
    nombre=models.CharField(max_length=50)
    rfc=models.CharField(max_length=15)
    cuenta=models.IntegerField()
    correo=models.CharField(max_length=50)
    fecha_nac=models.DateField()




    def __str__(self) -> str:
        return self.nombre
