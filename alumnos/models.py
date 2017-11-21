from django.db import models
from django.contrib import admin

class Alumno(models.Model):
    nombre  =   models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)

    def __str__(self):

        return self.nombre

class Materia(models.Model):
    nombre  =  models.CharField(max_length=40)
    nota = models.IntegerField()

    def __str__(self):

        return self.nombre

class Profesor(models.Model):
    nombre  =   models.CharField(max_length=15)
    apellido = models.CharField(max_length=15)
    materias   = models.ManyToManyField(Materia, through='AsignacionMat')
    def __str__(self):

        return self.nombre


class Grado(models.Model):
    nombre    = models.CharField(max_length=60)
    materias   = models.ManyToManyField(Materia, through='AsignacionGrad')
    alumnos = models.ManyToManyField(Alumno, through='AsignacionAlumno')
    def __str__(self):

        return self.nombre

class AsignacionMat(models.Model):

    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class AsignacionMatInLine(admin.TabularInline):

    model = AsignacionMat
    extra = 1

class ProfesorAdmin(admin.ModelAdmin):

    inlines = (AsignacionMatInLine,)

class MateriaAdmin (admin.ModelAdmin):

    inlines = (AsignacionMatInLine,)

class AsignacionGrad(models.Model):

    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

class AsignacionGradInLine(admin.TabularInline):

    model = AsignacionGrad
    extra = 1

class GradoAdmin(admin.ModelAdmin):

    inlines = (AsignacionGradInLine,)

class MateriaAdmin (admin.ModelAdmin):

    inlines = (AsignacionGradInLine,)

class AsignacionAlumno(models.Model):

    grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

class AsignacionAlumnoInLine(admin.TabularInline):

    model = AsignacionAlumno
    extra = 1

class GradoAdmin(admin.ModelAdmin):

    inlines = (AsignacionAlumnoInLine,)

class AlumnoAdmin (admin.ModelAdmin):

    inlines = (AsignacionAlumnoInLine,)
