from django.db import models
from persona.models import User
#from estructura.models import UserDispositivo

# Create your models here.
class Dispositivo(models.Model):
    #users = models.ManyToManyField(
    #    User,
    #    verbose_name='users',
    #    blank=True,
    #)

    nombre = models.CharField("Nombre del Controlador", max_length=30)

    class Meta:
        db_table = 'dispositivo'
        
    def __str__(self):
        return self.nombre


class TipoSensor(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipo_sensor'
        
    def __str__(self):
        return self.descripcion
        
        
class Sensor(models.Model):
    id_dispositivo_fk = models.ForeignKey(Dispositivo, 
                                          models.DO_NOTHING, 
                                          db_column='id_dispositivo_fk',
                                          verbose_name="Controlador",
                                          related_name='sensor')
    tipo = models.ForeignKey('TipoSensor',
                             models.DO_NOTHING,
                             db_column='id_tipo_sensor_fk',
                             verbose_name="Tipo de Sensor")

    descripcion = models.CharField("Descripción", max_length=20)

    class Meta:
        db_table = 'sensor'
        
    def __str__(self):
        return self.descripcion
    
    
class TipoActuador(models.Model):
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'tipo_actuador'
        
    def __str__(self):
        return self.descripcion


class Actuador(models.Model):
    id_dispositivo_fk = models.ForeignKey(Dispositivo, 
                                          models.DO_NOTHING, 
                                          db_column='id_dispositivo_fk',
                                          verbose_name="Controlador",
                                          related_name='actuador')
    tipo = models.ForeignKey('TipoActuador',
                             models.DO_NOTHING,
                             db_column='id_tipo_actuador_fk',
                             verbose_name="Tipo de Actuador")

    descripcion = models.CharField("Descripción", max_length=20)

    class Meta:
        db_table = 'actuador'
        
    def __str__(self):
        return self.descripcion


class PublicacionActuador(models.Model):
    id_actuador_fk = models.ForeignKey(Actuador, models.DO_NOTHING, db_column='id_actuador_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        db_table = 'publicacion_actuador'
        
    def __str__(self):
        return str(self.id_actuador_fk) + " | " + str(self.fecha)


class PublicacionSensor(models.Model):
    id_sensor_fk = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='id_sensor_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'publicacion_sensor'
        
    def __str__(self):
        return str(self.id_sensor_fk) + " | " + str(self.fecha)


class PublicacionControlador(models.Model):
    controlador = models.ForeignKey('Dispositivo', models.DO_NOTHING, db_column='controlador')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=1, decimal_places=0)

    class Meta:
        db_table = 'publicacion_controlador'
        
    def __str__(self):
        return str(self.controlador) + " | " + str(self.fecha)


        