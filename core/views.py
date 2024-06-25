from django.shortcuts import render, redirect
#from .zpoblar import poblar_bd
from .models import Producto
from .forms import IngresarForm, ProductoForm

def index(request):
    productos = Producto.objects.all().order_by('nombre')
    data = { 'productos': productos }
    return render(request, 'core/index.html', data)

def ficha(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    data = { 'producto': producto }
    return render(request, 'core/ficha.html', data)

def ingresar(request):
    # if request.user.is_authenticated:
    #     return redirect(index)
    form= IngresarForm()
    
    if request.method == 'POST':
        form= IngresarForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #... continua con la validacion de la cuenta de usuario
            
    return render(request, 'core/ingresar.html', {
        'form': IngresarForm(),
    })
    
def administracion(request):
    return render(request, 'core/administracion.html')

# def productos(request):
    #form= ProductoForm
    #return render(request, 'core/productos.html', {'form': form})
    
def productos(request):
    return render(request, 'core/productos.html')

def miscompras(request):
    return render(request, 'core/miscompras.html')

def nosotros(request):
    return render(request, 'core/nosotros.html')

def registro(request):
    return render(request, 'core/registro.html')

def misdatos(request):
    return render(request, 'core/misdatos.html')

def carrito(request):
    return render(request, 'core/carrito.html')

def usuarios(request):
    return render(request, 'core/usuarios.html')

def boleta(request):
    return render(request, 'core/boleta.html')

def ventas(request):
    return render(request, 'core/ventas.html')

def bodega(request):
    return render(request, 'core/bodega.html')

def ropa(request):
    return render(request, 'core/ropa.html')


# def poblar(request):
#     # Permite poblar la base de datos con valores de prueba en todas sus tablas.
#     # Opcionalmente se le puede enviar un correo único, para que los Administradores
#     # del sistema puedan probar el cambio de password de los usuarios, en la página
#     # de "Adminstración de usuarios".
#     poblar_bd('j.perez@duocuc.cl')
#     return redirect(index)