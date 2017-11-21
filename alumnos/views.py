from django.contrib import messages
from .forms import GradoForm
from alumnos.models import Grado, Alumno

def grado_nuevo(request):

    if request.method == "POST":

        formulario = GradoForm(request.POST)

        if formulario.is_valid():

            grado = Grado.objects.create(nombre=formulario.cleaned_data['nombre'])

            for grado_id in request.POST.getlist('grado'):

                asignaciongrad = asignaciongrad(grado_id=grado_id, alumno_id = alumno.id)

                asignaciongrad.save()

    else:

        formulario = PeliculaForm()

    return render(request, 'peliculas/pelicula_editar.html', {'formulario': formulario})

# Create your views here.
