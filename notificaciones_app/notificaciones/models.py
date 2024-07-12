from django.db import models
from django.utils import timezone

class Notificacion(models.Model):
    fecha_recepcion = models.DateField(default=timezone.now)
    hora_recepcion = models.TimeField(default=timezone.now)
    entidad_emisora = models.CharField(max_length=100)
    numero_cedula_expediente = models.CharField(max_length=50)
    dirigido_a = models.CharField(max_length=100)
    recepcionista = models.CharField(max_length=100, choices=[('Amanda González', 'Amanda González'), ('Wanda Pastor', 'Wanda Pastor')])
    colaborador_entrega = models.CharField(max_length=100, choices=[('Usuario1', 'Usuario1'), ('Usuario2', 'Usuario2')])
    fecha_hora_entrega = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.fecha_hora_entrega and not self.pk:
            print(f"Correo automático enviado a ptoribio@consortiumlegal.com indicando Notificación recibida: {self}")
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Notificación de {self.entidad_emisora} recibida el {self.fecha_recepcion} a las {self.hora_recepcion}"
