from django.urls import path
from sucursales_app import views

urlpatterns = [
    path("sucursales",views.sucursales,name="sucursales"),
    path("registrarSucursal/",views.registrarSucursal,name="registrarSucursal"),
    path("seleccionarSucursal/<id>",views.seleccionarSucursal,name="seleccionarSucursal"),
    path("editarSucursal/",views.editarSucursal, name="editarSucursal"),
    path("borrarSucursal/<id>",views.borrarSucursal,name="borrarSucursal"),
    
]