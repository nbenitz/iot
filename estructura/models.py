
from django.db import models
from persona.models import User
from dispositivo.models import Dispositivo


class UserDispositivo(models.Model):
    id_user_fk = models.ForeignKey(
        User, 
        models.DO_NOTHING, 
        db_column='id_user_fk',
        verbose_name='Usuario'
        )
    id_dispositivo_fk = models.ForeignKey(
        Dispositivo,
        models.DO_NOTHING,
        db_column='id_dispositivo_fk',
        verbose_name='Dispositivo'
        )

    class Meta:
        db_table = 'dispositivo_user'
        verbose_name='Dispositivos del Usuario'
        verbose_name_plural='Dispositivos del Usuario'
        unique_together = (('id_user_fk', 'id_dispositivo_fk'),)
        
    def __str__(self):
        return str(self.id_user_fk)

class Tablero(models.Model):
    id_user_fk = models.ForeignKey(
        User,
        models.DO_NOTHING,
        db_column='id_user_fk',
        verbose_name="Usuario")

    dispositivos = models.ManyToManyField(
        UserDispositivo,
        verbose_name='Dispositivos',
        blank=True,
    )

    nombre = models.CharField("Nombre del Tablero", max_length=30)

    class Meta:
        db_table = 'tablero'
        
    def __str__(self):
        return self.nombre