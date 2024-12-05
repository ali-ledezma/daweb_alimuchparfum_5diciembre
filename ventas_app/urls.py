from django.urls import path
from ventas_app import views

urlpatterns = [
    path("ventas",views.ventas,name="ventas"),
    path("registrarVenta/",views.registrarVenta,name="registrarVenta"),
    path("seleccionarVenta/<id>",views.seleccionarVenta,name="seleccionarVenta"),
    path("editarVenta/",views.editarVenta, name="editarVenta"),
    path("borrarVenta/<id>",views.borrarVenta,name="borrarVenta"),
    
]