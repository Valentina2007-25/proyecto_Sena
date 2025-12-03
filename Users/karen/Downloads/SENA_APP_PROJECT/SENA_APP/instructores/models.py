from django.db import models

# Create your models here.
class Instructor(models.Model):
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('TI', 'Tarjeta de Identidad'),
        ('PP', 'Pasaporte'),
    ]
    NIVEL_EDUCACION_CHOICES = [
        ('TEC', 'Técnico'),
        ('TGL', 'Tecnólogo'),
        ('PRE', 'Pregrado'),
        ('ESP', 'Especialización'),
        ('MAE', 'Maestría'),
        ('DOC', 'Doctorado'),
    ]
    
    
    documento_identidad = models.CharField(max_length=20, unique=True)
    tipo_documento = models.CharField(max_length=3, choices=TIPO_DOCUMENTO_CHOICES, default='CC')
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    correo = models.EmailField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now=True)
    ciudad = models.CharField(max_length=100)
    nivel_educacion = models.CharField(max_length=3, choices=NIVEL_EDUCACION_CHOICES)
    especialidad = models.CharField(max_length=100)
    anos_experiencia = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)
    fecha_vinculacion = models.DateField()
    fecha_registro = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.especialidad}"
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"