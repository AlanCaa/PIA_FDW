from django.urls import path
from .views import index, contacto, sucursales, productos, empleado, clientes

urlpatterns = [
    path('', index, name='index'),
    path('productos/', productos, name='productos'),
    path('sucursales/', sucursales, name='sucursales'),
    path('contacto/', contacto, name='contacto'),
    path('empleado/', empleado, name='empleado'),
    path('clientes/', clientes, name='clientes'),
    # path('premios/', index, name='index'),
    # path('productos/', index, name='index'),
]
