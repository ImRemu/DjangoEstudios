from django.db import models
from django.utils import timezone

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.nombre
# cascade: eliminar el producto
# protect: lanza error
# restrict: solo elimina si no existe
# set_null: actualiza a valor nulo 
# set_default: asigna valor por defecto
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(default=timezone.now)
    def __str__(self) -> str:
        return self.nombre