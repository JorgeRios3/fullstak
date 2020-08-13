from django.db import models


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido_paterno = models.CharField(max_length=20, blank=True, null=True)
    apellido_materno = models.CharField(max_length=20, blank=True, null=True)
    edad = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'personas'


class Viaje(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    fecha_creacion = models.DateField()
    capacidad_personas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    #publications = models.ManyToManyField(Publication)
    class Meta:
        db_table = 'viajes'


class Pago(models.Model):
    fecha = models.CharField(max_length=50)
    total = models.CharField(max_length=20)
    persona = models.ForeignKey(Persona, related_name='pagos', on_delete=models.CASCADE)
    viaje = models.ForeignKey(Viaje, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pagos'

    def __str__(self):
        return 'fecha {}'.format(self.total)
