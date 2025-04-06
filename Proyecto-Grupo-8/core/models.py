
# Create your models here.
from django.db import models
from authentication.models import User

#registro de medidas, generación de informes, visualización consolidada, envío de alertas y gestión de permisos
#configuración inicial del sistema: creación de planes, tipos de medida, regiones (fixtures)
#Faltan modelos que representen la lógica de generación de informes anuales consolidados, incluyendo indicadores clave y exportación.
#No se observan validaciones o restricciones adicionales en los modelos (por ejemplo, unicidad de combinaciones, longitud mínima).

class Organismo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    contacto = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class PlanDescontaminacion(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    region = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_inicio = models.DateField() # soporta directamente el formato ISO 8601 -> YYYY-MM-DD
    fecha_fin = models.DateField(blank=True, null=True)
    medidas = models.ManyToManyField('core.Medida', blank=True, related_name='planes') #[1,2,4]

    def __str__(self):
        return self.nombre

class TipoMedida(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# SMA - Mediante analista SMA publica una medida
class Medida(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completado', 'Completado'),
    ]
    organismo = models.ForeignKey(Organismo, on_delete=models.SET_NULL, null=True, blank=True)
    tipo_medida = models.ForeignKey(TipoMedida, on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=255, null=False)
    indicador = models.CharField(max_length=255)
    formula_calculo = models.TextField()
    frecuencia_reporte = models.CharField(max_length=50, blank=True, null=True)
    medio_verificacion = models.TextField()
    estado = models.CharField(max_length=50, choices=ESTADO_CHOICES, default='pendiente')

    def __str__(self):
        return f"{self.nombre} - {self.estado}"


# Organismo Sectoral - Mediante el funcinario sectorial publica un reporte a la SMA.
# SMA - Mediante analista SMA puede ver el reporte.
class Reporte(models.Model): 
    medida = models.ForeignKey("core.Medida", on_delete=models.CASCADE, related_name='reportes')
    titutlo = models.CharField(max_length=255)
    creador = models.ForeignKey("authentication.User", on_delete=models.SET_NULL, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    medio_verificacion_archivo = models.FileField(upload_to='medios_verificacion/', blank=True, null=True)

    def __str__(self):
        return f"{self.titutlo} - {self.fecha_creacion}"

    

#revisar, faltan cosas. Se  incluye  un  modelo  adicional  RegistroMedida,  lo  que  sugiere  una preocupación por la trazabilidad temporal de los reportes. 
class RegistroMedida(models.Model):
    medida = models.ForeignKey(Medida, on_delete=models.CASCADE, related_name='registros')
    usuario_registro = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.medida.nombre} - {self.fecha_registro}"


