from django.db import models

# Create your models here.

class Motos(models.Model):
    id= models.AutoField(primary_key=True)
    marca = models.CharField(max_length=100, verbose_name='Marca') 
    imagen = models.ImageField(upload_to='imagenes/',verbose_name="Imagen", null=True)
    nombre = models.TextField(verbose_name="Nombre", null=True)

    def __str__(self):
        fila = "Moto: " + self.marca + " - " + self.nombre
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()