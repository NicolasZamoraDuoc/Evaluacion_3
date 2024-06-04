from django.urls import path
from .views import index

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
    path('', productos, name="v"),
    path('', registro, name="registro"),
    path('', ropa, name="ropa"),
    path('', usuarios, name="usuarios"),
    path('', ventas, name="ventas"),
]
