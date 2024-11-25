from django.shortcuts import render
from django.http import HttpResponse
from App_00.models import Curso, Profesor, Entregable, Estudiante
from App_00.forms import CursoFormulario, EstudianteFormulario, ProfesorFormulario
# Create your views here.

def inicio(req):
    return render(req, 'app_00/padre.html')

# ---------------------------- CURSOS ----------------------------------
def cursos(req):
    return render(req, 'app_00/cursos.html')

def cursoForm(req):

    if req.method == 'POST':
      
        curso =  Curso(nombre=req.POST['curso'],camada=req.POST['camada'])

        curso.save()

        return render(req, "app_00/padre.html")
    
    # GET
    return render(req, 'app_00/cursoForm.html')

def cursoForm2(req):

    if req.method == 'POST':
        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada = informacion["camada"])
            curso.save()
            return render(req, "app_00/index.html")
    else:
        miFormulario = CursoFormulario()
    # GET
    return render(req, 'app_00/cursoForm2.html', {"miFormulario": miFormulario})
# -----------------------------------------------------------------------
def profesores(req):
    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profe = Profesor(nombre=informacion["nombre"], apellido = informacion["apellido"], email=informacion['email'], profesion=informacion['profesion'])
            profe.save()
            return render(req, "app_00/index.html")
    else:
        miFormulario = ProfesorFormulario()
    # GET
    return render(req, 'app_00/profesores.html', {"miFormulario": miFormulario})

def estudiantes(req):

    if req.method == 'POST':
        miFormulario = EstudianteFormulario(req.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            estudiante = Estudiante(nombre=informacion["nombre"], apellido = informacion["apellido"], email=informacion['email'])
            estudiante.save()
            return render(req, "app_00/index.html")
    else:
        miFormulario = EstudianteFormulario()
    # GET
    return render(req, 'app_00/estudiantes.html', {"miFormulario": miFormulario})

def entregables(req):
    return render(req, 'app_00/entregables.html')

def busquedaCamada(req):
    return render(req, 'app_00/busquedaCamada.html')

def buscar(req):
    if req.GET["camada"]:

        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(req, "app_00/resultadosBusqueda.html", {"cursos": cursos, "camada": camada})
    else:
        return HttpResponse("No hay datos")
