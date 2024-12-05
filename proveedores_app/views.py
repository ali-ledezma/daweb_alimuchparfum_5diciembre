from django.shortcuts import render, redirect
from .models import Proveedor
# Create your views here.
def proveedores(request):
    losproveedores=Proveedor.objects.all()
    return render(request,'gestionarProveedores.html',{"misproveedores":losproveedores})

def registrarProveedor(request):
    idproveedor=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    rfc=request.POST["txtrfc"]
    telefono=request.POST["numtelefono"]
    direccion=request.POST["txtdireccion"]




    guardarProveedor=Proveedor.objects.create(
        idproveedor=idproveedor,
        nombre=nombre,
        rfc=rfc,
        direccion=direccion,
        telefono=telefono,
        )
    
    return redirect ("proveedores")

def seleccionarProveedor(request,idproveedor):
    proveedor=Proveedor.objects.get(idproveedor=idproveedor)
    return render(request,"editarProveedores.html",{"misproveedores":proveedor})


def editarProveedor(request):
    idproveedor=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    rfc=request.POST["txtrfc"]
    direccion=request.POST["txtdireccion"]
    telefono=request.POST["numtelefono"]
    proveedor=Proveedor.objects.get(idproveedor=idproveedor)
    proveedor.nombre=nombre
    proveedor.rfc=rfc
    proveedor.direccion=direccion
    proveedor.telefono=telefono
    proveedor.save()
    return redirect("proveedores") #dsf


def borrarProveedor(request,idproveedor):
    proveedor=Proveedor.objects.get(idproveedor=idproveedor)
    proveedor.delete()
    return redirect("proveedores") #asdsda
