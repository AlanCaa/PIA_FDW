from django.shortcuts import render
from .models import Producto, Sucursal, Empleado, Cliente
# Create your views here.
def index(request):
    return render(request,'index.html')

def productos(request):
    datos = {
        'productos': Producto.objects.all()
    }
    return render(request, "productos.html", context=datos)

def empleado(request):
    datos = {
        'empleado': Empleado.objects.all()
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

