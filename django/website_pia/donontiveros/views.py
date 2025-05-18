from django.shortcuts import render
from .models import Producto, Sucursal, Empleado, Cliente, Contacto
# Create your views here.
def index(request):
    return render(request,'index.html')

def productos(request):
    datos = {
        'productos': Producto.objects.all()
    }
    return render(request, "productos.html", context=datos)

def empleado(request):
    #sucursal_id = request.GET.get('sucursal')
    try:
        sucursal_id = int(request.GET.get('sucursal')) if request.GET.get('sucursal') else None
    except ValueError:
        sucursal_id = None
    
    empleados = Empleado.objects.all()

    if sucursal_id:
        empleados = empleados.filter(sucursal_id=sucursal_id)

    datos = {
        'empleado': empleados,
        'sucursales': Sucursal.objects.all(),
        'sucursal_seleccionada': sucursal_id
    }
    return render(request, "empleado.html", context=datos)

def sucursales(request):
    datos = {
        'sucursales': Sucursal.objects.all()
    }
    return render(request, "sucursales.html", context=datos)

def contacto(request):
    return render(request,'contacto.html')

def clientes(request):
    datos = {
        'clientes': Cliente.objects.all()
    }
    return render(request,'clientes.html', context=datos)

def contacto(request):
    datos = {
        'contacto': Contacto.objects.all()
    }
    return render(request,'contacto.html', context=datos)

