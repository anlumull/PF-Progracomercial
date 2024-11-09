from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique = True)
    password = models.CharField(max_length=255)

    first_name = None
    last_name = None
    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Alumno(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll = models.CharField(max_length=100, default='Alumno')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"
    
class Maestro(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    roll = models.CharField(max_length=100, default='Maestro')

    def __str__(self):
        return f"{self.nombres} {self.apellidos}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    semestre = models.CharField(max_length=20)
    maestro = models.ForeignKey(Maestro, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class AsignacionCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    fecha_asignacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.alumno} -> {self.curso}"
    
class Tarea(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=200)
    fecha_entrega = models.DateField(null=True, max_length=50)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
        