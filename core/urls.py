from django.urls import path
from .views import index
from .views import administracion
from .views import bodega
from .views import boleta
from .views import carrito
from .views import ficha
from .views import ingresar
from .views import miscompras
from .views import misdatos
from .views import nosotros
from .views import productos
from .views import registro
from .views import ropa
from .views import usuarios
from .views import ventas

urlpatterns = [
    path('', index, name="index"),
    path('', administracion, name="administracion"),
    path('', bodega, name="bodega"),
    path('', boleta, name="boleta"),
    path('', carrito, name="carrito"),
    path('', ficha, name="ficha"),
    path('', ingresar, name="ingresar"),
    path('', miscompras, name="miscompras"),
    path('', misdatos, name="misdatos"),
    path('', nosotros, name="nosotros"),
    path('', productos, name="productos"),
    path('', registro, name="registro"),
    path('', ropa, name="ropa"),
    path('', usuarios, name="usuarios"),
    path('', ventas, name="ventas"),
]
