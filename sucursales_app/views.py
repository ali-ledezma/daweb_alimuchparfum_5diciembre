from django.shortcuts import render, redirect
from .models import Sucursal
# Create your views here.
def sucursales(request):
    lassucursales=Sucursal.objects.all()
    return render(request,'gestionarSucursales.html',{"missucursales":lassucursales})

def registrarSucursal(request):
    id = request.POST["txtid"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    numero = request.POST["numnumero"]
    nombre = request.POST["txtnombre"]
    cempleados = request.POST["numcempleados"]




    guardarSucursal=Sucursal.objects.create(
        id=id,direccion=direccion,telefono=telefono,correo=correo,numero=numero,nombre=nombre,cempleados=cempleados
    ) 
    return redirect ("sucursales")

def seleccionarSucursal(request,id):
    sucursal=Sucursal.objects.get(id=id)
    return render(request,"editarSucursales.html",{"missucursales":sucursal})


def editarSucursal(request):
    id = request.POST["txtid"]
    direccion = request.POST["txtdireccion"]
    telefono = request.POST["txttelefono"]
    correo = request.POST["txtcorreo"]
    numero = request.POST["numnumero"]
    nombre = request.POST["txtnombre"]
    cempleados = request.POST["numcempleados"]
    sucursal=Sucursal.objects.get(id=id)
    sucursal.id=id
    sucursal.direccion=direccion
    sucursal.telefono=telefono
    
    sucursal.correo=correo
    
    sucursal.numero=numero
    
    sucursal.nombre=nombre
    
    sucursal.cempleados=cempleados

    sucursal.save()
    return redirect("sucursales") #dsf


def borrarSucursal(request,id):
    sucursal=Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect("sucursales") #asdsda
