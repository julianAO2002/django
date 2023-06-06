from .models import Curso, Profesor, Alumno
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404, HttpResponseRedirect
from . import forms 
from django.urls import reverse



def index(request):
    return render(request, "myapp/index.html" )

def acerca_de ( request ):
    return HttpResponse( "¡Curso de Python y Django!" )

def cursos(request):
    cursos = Curso.objects.all()
    ctx = {"cursos": cursos}
    return render(request, "myapp/cursos.html", ctx)

def cursos_json(request):
    response = JsonResponse(list(Curso.objects.values()), safe=False)
    return response

def curso(request, id):
    curso = Curso.objects.get(id=id)
    if curso:
        ctx = {"curso": curso}
        return render(request, "myapp/curso.html", ctx)
    else:
        raise Http404("No se encontraron cursos con el nombre proporcionado.")    
   

def nuevo_curso(request):
    if request.method == "POST":
        form = forms.FormularioCurso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioCurso()
        ctx = {"form": form}
        return render(request, "myapp/nuevo_curso.html", ctx)
    
def profesores(request):
    profesores = Profesor.objects.all()
    ctx = {"profesores": profesores}
    return render(request, "myapp/profesores.html", ctx)
    

def nuevo_profesor(request):
    if request.method == "POST":
        form = forms.FormularioProfesor(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("cursos"))
    else:
        form = forms.FormularioProfesor()
        ctx = {"form": form}
        return render(request, "myapp/nuevo_profesor.html", ctx)   

def profesor(request, id):
    profesor = Profesor.objects.get(id=id)
    if profesor:
        ctx = {"profesor": profesor}
        return render(request, "myapp/profesor.html", ctx)
    else:
        raise Http404("No se encontraron profesor con el nombre proporcionado.") 
    
def alumnos(request):
    alumnos = Alumno.objects.all()
    ctx = {"alumnos": alumnos}
    return render(request, "myapp/alumnos.html", ctx)

def nuevo_alumno(request):
    if request.method == "POST":
        form = forms.FormularioAlumno(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("alumnos"))
    else:
        form = forms.FormularioAlumno()
        ctx = {"form": form}
        return render(request, "myapp/nuevo_alumno.html", ctx)
    
def alumno(request, id):
    alumno = Alumno.objects.get(id=id)
    if alumno:
        ctx = {"alumno": alumno}
        return render(request, "myapp/alumno.html", ctx)
    else:
        raise Http404("No se encontraron profesor con el nombre proporcionado.") 
