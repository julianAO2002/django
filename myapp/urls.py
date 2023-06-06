from django.urls import path
from . import views



urlpatterns = [
    path( "" , views.index, name = "index" ),
    path( "acerca-de" , views.acerca_de, name = "acerca_de" ),
    path( "cursos" , views.cursos, name = "cursos" ),
    path( "cursos/json" , views.cursos_json, name = "cursos_json" ),
    path("curso/<str:id>", views.curso, name="curso"),
    path("nuevo-curso", views.nuevo_curso, name="nuevo_curso"),
    path("profesores", views.profesores, name="profesores"),
    path("nuevo-profesor", views.nuevo_profesor, name="nuevo_profesor"), 
    path("profesor/<str:id>", views.profesor, name="profesor"),
    path("alumnos", views.alumnos, name="alumnos"),
    path("nuevo-alumno", views.nuevo_alumno, name="nuevo_alumno"),
    path("alumno/<str:id>", views.alumno, name="alumno"),     
]