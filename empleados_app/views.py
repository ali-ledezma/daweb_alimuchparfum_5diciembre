from django.shortcuts import render, redirect
from .models import Empleado
# Create your views here.
def empleados(request):
    losempleados=Empleado.objects.all()
    return render(request,'gestionarEmpleados.html',{"misempleados":losempleados})

def registrarEmpleado(request):
    idempleados = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    fecha_ingreso=request.POST["datafec"]
    salario = request.POST["numsalario"]
    curp = request.POST["txtcurp"]
    idsucursal = request.POST["txtids"]
    puesto=request.POST["txtpuesto"]




    guardarEmpleado=Empleado.objects.create(
        idempleados=idempleados, 
        nombre=nombre,
        telefono=telefono,
        fecha_ingreso=fecha_ingreso,
        salario=salario,
        curp=curp,
        idsucursal=idsucursal
        ,puesto=puesto
       
    ) 
    return redirect ("empleados")

def seleccionarEmpleado(request,idempleados):
    empleado=Empleado.objects.get(idempleados=idempleados)
    return render(request,"editarEmpleados.html",{"misempleados":empleado})


def editarEmpleado(request):
    idempleados = request.POST["txtid"]
    nombre = request.POST["txtnombre"]
    telefono = request.POST["numtelefono"]
    fecha_ingreso=request.POST["datafec"]
    salario = request.POST["numsalario"]
    curp = request.POST["txtcurp"]
    idsucursal = request.POST["txtids"]
    puesto=request.POST["txtpuesto"]

   
    empleado=Empleado.objects.get(idempleados=idempleados)
    empleado.idempleados=idempleados
    empleado.nombre=nombre
    empleado.telefono=telefono
    empleado.salario=salario
    empleado.curp=curp
    empleado.idsucursal=idsucursal
    empleado.puesto=puesto
    empleado.fecha_ingreso=fecha_ingreso

    empleado.save()
    return redirect("empleados") #dsf


def borrarEmpleado(request,idempleados):
    empleado=Empleado.objects.get(idempleados=idempleados)
    empleado.delete()
    return redirect("empleados") #asdsda
