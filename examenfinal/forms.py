from django import forms

from .models import Grado, Materia, Alumno


class GradoForm(forms.ModelForm):
#todos los campos de Pelicula
    class Meta:
        model = Grado
        fields = ('nombre','actores')
def __init__ (self, *args, **kwargs):

#En este caso vamos a usar el widget checkbox multiseleccionable.

        self.fields["alumnos"].widget = forms.widgets.CheckboxSelectMultiple()

#Podemos usar un texto de ayuda en el widget

       self.fields["alumnos"].help_text = "Ingrese los alumnos del curso"

#En este caso le indicamos que nos muestre todos los actores, pero aquí podríamos filtrar datos si fuera necesario

        self.fields["alumnos"].queryset = Alumno.objects.all()
