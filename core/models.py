from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    anio = models.CharField(max_length=4)  # Asegúrate de definir max_length para anio
    categoria = models.CharField(max_length=50)  # Asegúrate de definir max_length para categoria
    descripcion = models.CharField(max_length=255)  # Asegúrate de definir max_length para descripcion
    precio = models.CharField(max_length=10)  # Asegúrate de definir max_length para precio

    def __str__(self):
        return f"{self.titulo} {self.anio}"
    

class Autores(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Categorias(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre
