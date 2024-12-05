from django.shortcuts import render, redirect
from .models import Cliente
# Create your views here.
def clientes(request):
    losclientes=Cliente.objects.all()
    return render(request,'gestionarClientes.html',{"misclientes":losclientes})

def registrarCliente(request):
    idcliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    rfc = request.POST["txtrfc"]
    cuenta = request.POST["numcuenta"]
    correo = request.POST["txtcorreo"]
    fecha_nac = request.POST["datefec"]




    guardarCliente=Cliente.objects.create(
        idcliente=idcliente,
        nombre=nombre,
        rfc=rfc,
        cuenta=cuenta,
        correo=correo,
        fecha_nac=fecha_nac

    
       
    ) 
    return redirect ("clientes")

def seleccionarCliente(request,idcliente):
    cliente=Cliente.objects.get(idcliente=idcliente)
    return render(request,"editarClientes.html",{"misclientes":cliente})


def editarCliente(request):
    idcliente = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    rfc = request.POST["txtrfc"]
    cuenta = request.POST["numcuenta"]
    correo = request.POST["txtcorreo"]
    fecha_nac = request.POST["datefec"]

   
    cliente=Cliente.objects.get(idcliente=idcliente)
    cliente.idcliente=idcliente
    cliente.nombre=nombre
    cliente.rfc=rfc
    cliente.cuenta=cuenta
    cliente.correo=correo
    cliente.fecha_nac=fecha_nac

    cliente.save()
    return redirect("clientes") #dsf


def borrarCliente(request,idcliente):
    cliente=Cliente.objects.get(idcliente=idcliente)
    cliente.delete()
    return redirect("clientes") #asdsda
