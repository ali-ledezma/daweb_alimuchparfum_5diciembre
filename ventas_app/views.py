from django.shortcuts import render, redirect
from .models import Ventas
# Create your views here.
def ventas(request):
    lasventas = Ventas.objects.all()
    return render(request, 'gestionarVentas.html', {"misventas": lasventas})

def registrarVenta(request):
    id = request.POST["txtid"]
    fecha_venta = request.POST["datefecha_venta"]
    cantidad = request.POST["numcantidad"]
    total = request.POST["numtotal"]
    idsucursal = request.POST["numidsucursal"]
    idproducto = request.POST["numidproducto"]
    idempleado = request.POST["numidempleado"]
    idcliente = request.POST["numidcliente"]

    guardarVenta = Ventas.objects.create(
        id = id,
        fecha_venta = fecha_venta,
        cantidad = cantidad,
        total = total,
        idsucursal = idsucursal,
        idproducto = idproducto,
        idempleado = idempleado,
        idcliente = idcliente
    ) 
    return redirect("ventas")

def seleccionarVenta(request, id):
    venta = Ventas.objects.get(id=id)
    return render(request, "editarVentas.html", {"misventas": venta})

def editarVenta(request):
    id = request.POST["txtid"]
    fecha_venta = request.POST["datefecha_venta"]
    cantidad = request.POST["numcantidad"]
    total = request.POST["numtotal"]
    idsucursal = request.POST["numidsucursal"]
    idproducto = request.POST["numidproducto"]
    idempleado = request.POST["numidempleado"]
    idcliente = request.POST["numidcliente"]
    venta = Ventas.objects.get(id=id)
    venta.fecha_venta = fecha_venta
    venta.cantidad = cantidad
    venta.total = total
    venta.idsucursal = idsucursal
    venta.idproducto = idproducto
    venta.idempleado = idempleado
    venta.idcliente = idcliente

    venta.save()
    return redirect("ventas")

def borrarVenta(request, id):
    venta = Ventas.objects.get(id=id)
    venta.delete()
    return redirect("ventas")
