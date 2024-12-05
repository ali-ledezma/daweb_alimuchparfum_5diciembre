from django.urls import path
from empleados_app import views

urlpatterns = [
    path("empleados",views.empleados,name="empleados"),
    path("registrarEmpleado/",views.registrarEmpleado,name="registrarEmpleado"),
    path("seleccionarEmpleado/<idempleados>",views.seleccionarEmpleado,name="seleccionarEmpleado"),
    path("editarEmpleado/",views.editarEmpleado, name="editarEmpleado"),
    path("borrarEmpleado/<idempleados>",views.borrarEmpleado,name="borrarEmpleado"),
    
]