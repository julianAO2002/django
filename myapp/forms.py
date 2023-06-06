from django.forms import ModelForm
from .models import Curso, Profesor, Alumno


class FormularioCurso(ModelForm):
    class Meta:
        model = Curso
        fields = ("nombre", "inscriptos", "turno", "profesor")

class FormularioProfesor(ModelForm):
    class Meta:
        model = Profesor
        fields = ("nombre","email","telefono","cuit", "monotributista", "cursos")  
class FormularioAlumno(ModelForm):
    class Meta:
        model = Alumno
        fields = ("nombre","email","telefono","dni", "cursos")