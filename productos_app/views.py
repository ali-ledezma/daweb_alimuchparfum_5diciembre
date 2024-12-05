from django.shortcuts import render, redirect
from .models import Producto
# Create your views here.
def index(request):
    return render(request, 'index.html')

def productos(request):
    losproductos=Producto.objects.all()
    return render(request,'gestionarProductos.html',{"misproductos":losproductos})

def registrarProducto(request):
    idproducto=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    idsucursal=request.POST["numidsucursal"]
    marca=request.POST["txtmarca"]
    stock=request.POST["numstock"]
    idproveedor=request.POST["txtpro"]
    notas=request.POST["txtnotas"]



    guardarProducto=Producto.objects.create(
        idproducto=idproducto,nombre=nombre,idsucursal=idsucursal,marca=marca,stock=stock,idproveedor=idproveedor,notas=notas
    ) 
    return redirect ("productos")

def seleccionarProducto(request,idproducto):
    producto=Producto.objects.get(idproducto=idproducto)
    return render(request,"editarProductos.html",{"misproductos":producto})


def editarProducto(request):
    idproducto=request.POST["txtid"]
    nombre=request.POST["txtnombre"]
    idsucursal=request.POST["numidsucursal"]
    marca=request.POST["txtmarca"]
    stock=request.POST["numstock"]
    idproveedor=request.POST["txtpro"]
    notas=request.POST["txtnotas"]
    producto=Producto.objects.get(idproducto=idproducto)
    producto.nombre=nombre
    producto.idsucursal=idsucursal
    producto.marca=marca
    producto.stock=stock
    producto.idproveedor=idproveedor
    producto.notas=notas
    producto.save()
    return redirect("productos") #dsf


def borrarProducto(request,idproducto):
    producto=Producto.objects.get(idproducto=idproducto)
    producto.delete()
    return redirect("productos") #asdsda
