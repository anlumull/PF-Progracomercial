from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Alumno)
admin.site.register(Maestro)
admin.site.register(Curso)
admin.site.register(AsignacionCurso)
admin.site.register(Tarea)