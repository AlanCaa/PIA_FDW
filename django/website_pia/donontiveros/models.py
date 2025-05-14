from django.db import models

# Create your models here.
class Producto(models.Model):
    descripcion = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    material = models.CharField(max_length=45)
    imagen = models.CharField(max_length=200)
    precio = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion
    
class Sucursal(models.Model):
    descripcion = models.CharField(max_length=45)
    direccion = models.CharField(max_length=200)
    imagen = models.CharField(max_length=200)
    horario = models.CharField(max_length=45)
    telefonos = models.CharField(max_length=50)
    def __str__(self):
        return self.descripcion