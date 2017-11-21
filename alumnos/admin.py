from django.contrib import admin
from alumnos.models import Alumno, AlumnoAdmin, Grado, GradoAdmin, Materia, MateriaAdmin, Profesor, ProfesorAdmin

#Registramos nuestras clases principales.
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Materia, MateriaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
