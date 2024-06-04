from django.shortcuts import redirect, render

# Create your views here.

def index(request):
    data={'nombre':'Chris Evans',
        'productos':Producto.objects.all().order_by('nombre')}
    return render(request, "core/index.html",data)

def administracion(request):
    return render(request, "core/administracion.html")
def bodega(request):
    return render(request, "core/bodega.html")
def boleta(request):
    return render(request, "core/boleta.html")
def carrito(request):
    return render(request, "core/carrito.html")
def ficha(request):
    return render(request, "core/ficha.html")
def ingresar(request):
    return render(request, "core/ingresar.html")
def miscompras(request):
    return render(request, "core/miscompras.html")
def misdatos(request):
    return render(request, "core/misdatos.html")
def nosotros(request):
    return render(request, "core/nosotros.html")
def productos(request):
    return render(request, "core/productos.html")
def registro(request):
    return render(request, "core/registro.html")
def ropa(request):
    return render(request, "core/ropa.html")
def usuarios(request):
    return render(request, "core/usuarios.html")
def ventas(request):
    return render(request, "core/ventas.html")
