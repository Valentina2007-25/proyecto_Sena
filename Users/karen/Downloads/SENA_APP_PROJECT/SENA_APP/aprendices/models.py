from django.db import models

# Create your models here.

class Aprendiz(models.Model):
    documento = models.CharField(max_length=20, unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now=True)
    ciudad = models.CharField(max_length=100)
    programa = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"