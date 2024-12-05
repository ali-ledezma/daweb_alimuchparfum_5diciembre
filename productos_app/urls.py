from django.urls import path
from productos_app import views

urlpatterns = [
    path("",views.index,name="index"),
    path("productos",views.productos,name="productos"),
    path("registrarProducto/",views.registrarProducto,name="registrarProducto"),
    path("seleccionarProducto/<idproducto>",views.seleccionarProducto,name="seleccionarProducto"),
    path("editarProducto/",views.editarProducto, name="editarProducto"),
    path("borrarProducto/<idproducto>",views.borrarProducto,name="borrarProducto"),
    
]