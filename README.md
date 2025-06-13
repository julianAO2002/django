# Proyecto Django - Gestión de Cursos, Profesores y Alumnos

Este proyecto es una aplicación web desarrollada con Django para gestionar cursos, profesores y alumnos. Permite visualizar listados, detalles y crear nuevas entidades a través de formularios.

---

## Modelos

### Curso
Representa un curso con los siguientes campos:

- `nombre` (CharField): Nombre del curso.
- `inscriptos` (IntegerField): Cantidad de inscriptos.
- `turno` (PositiveSmallIntegerField): Turno del curso, puede ser:
  - 1: Mañana
  - 2: Tarde
  - 3: Noche
- `profesor` (ForeignKey a Profesor): Profesor principal que dicta el curso (puede ser nulo).

### Profesor
Representa un profesor con datos personales y laborales:

- `nombre` (CharField): Nombre completo.
- `email` (EmailField): Correo electrónico.
- `telefono` (CharField): Número telefónico.
- `cuit` (CharField): CUIT del profesor.
- `monotributista` (BooleanField): Indica si el profesor es monotributista.
- `cursos` (ManyToManyField a Curso): Relación muchos a muchos con los cursos que dicta.

### Alumno
Representa un alumno con información básica y cursos en los que está inscripto:

- `nombre` (CharField): Nombre completo.
- `email` (EmailField): Correo electrónico.
- `telefono` (CharField): Número telefónico.
- `dni` (CharField): Documento Nacional de Identidad.
- `cursos` (ManyToManyField a Curso): Cursos en los que está inscripto.

---

## Vistas (funciones principales)

- `index`: Página principal, muestra una vista básica.

- `acerca_de`: Respuesta simple con texto indicando el curso (mensaje estático).

- `cursos`: Muestra un listado de todos los cursos disponibles, pasando los datos a la plantilla `cursos.html`.

- `cursos_json`: Devuelve un JSON con todos los cursos (útil para APIs o integraciones).

- `curso`: Muestra el detalle de un curso específico identificado por `id`.

- `nuevo_curso`: Permite crear un nuevo curso mediante un formulario. Si la petición es POST y el formulario es válido, guarda el curso y redirige al listado.

- `profesores`: Lista todos los profesores registrados.

- `nuevo_profesor`: Formulario para agregar un nuevo profesor.

- `profesor`: Muestra detalles de un profesor por `id`.

- `alumnos`: Lista todos los alumnos registrados.

- `nuevo_alumno`: Formulario para agregar un nuevo alumno.

- `alumno`: Muestra detalles de un alumno por `id`.

---

## URLs

Las rutas definidas permiten acceder a las vistas mencionadas, por ejemplo:

- `/` → `index`
- `/acerca-de` → `acerca_de`
- `/cursos` → listado de cursos
- `/cursos/json` → cursos en formato JSON
- `/curso/<id>` → detalle de un curso
- `/nuevo-curso` → crear curso
- `/profesores` → listado profesores
- `/nuevo-profesor` → crear profesor
- `/profesor/<id>` → detalle profesor
- `/alumnos` → listado alumnos
- `/nuevo-alumno` → crear alumno
- `/alumno/<id>` → detalle alumno

---


