from django.urls import path
from .views import index, contacto, sucursales, productos

urlpatterns = [
    path('', index, name='index'),
    path('productos/', productos, name='productos'),
    path('sucursales/', sucursales, name='sucursales'),
    path('contacto/', contacto, name='contacto'),
    # path('clientes/', index, name='index'),
    # path('premios/', index, name='index'),
    # path('productos/', index, name='index'),
]
