from django.urls import path
from proveedores_app import views

urlpatterns = [
    path("proveedores",views.proveedores,name="proveedores"),
    path("registrarProveedor/",views.registrarProveedor,name="registrarProveedor"),
    path("seleccionarProveedor/<idproveedor>",views.seleccionarProveedor,name="seleccionarProveedor"),
    path("editarProveedor/",views.editarProveedor, name="editarProveedor"),
    path("borrarProveedor/<idproveedor>",views.borrarProveedor,name="borrarProveedor"),
    
]