from django.db import models


class Curso(models.Model):
    nombre = models.CharField(max_length=128)
    inscriptos = models.IntegerField()
    TURNOS = (
    (1, "Mañana"),
    (2, "Tarde"),
    (3, "Noche")
    )
    turno = models.PositiveSmallIntegerField("Turnos",choices=TURNOS, null=True,)
    profesor = models.ForeignKey(
        "Profesor",
        on_delete=models.SET_NULL,
        null=True,
        related_name="cursos_dictados",
        
        )
    
    def __str__(self):
        return (self.nombre)
    

class Profesor(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    cuit = models.CharField(max_length=11)
    monotributista = models.BooleanField()
    cursos = models.ManyToManyField(Curso, related_name="profesores")

    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Profesores"

class Alumno(models.Model):
    nombre = models.CharField(max_length=128)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=11)    
    cursos = models.ManyToManyField(Curso, related_name="alumnos")

    
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Alumnos"    