from django.db import models
from estructura.models import Topic

# Create your models here.
class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    id_topic_fk = models.ForeignKey(Topic,
                                    models.DO_NOTHING,
                                    db_column='id_topic_fk',
                                    verbose_name="Topic o Grupo al que pertenece")
    nombre = models.CharField("Nombre del Controlador", max_length=30)

    class Meta:
        managed = True
        db_table = 'dispositivo'
        
    def __str__(self):
        return self.nombre


class TipoSensor(models.Model):
    id_tipo_sensor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo_sensor'
        
    def __str__(self):
        return self.descripcion
        
        
class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    id_dispositivo_fk = models.ForeignKey(Dispositivo, 
                                          models.DO_NOTHING, 
                                          db_column='id_dispositivo_fk',
                                          verbose_name="Controlador")
    id_tipo_sensor_fk = models.ForeignKey('TipoSensor', 
                                          models.DO_NOTHING, 
                                          db_column='id_tipo_sensor_fk',
                                          verbose_name="Tipo de Sensor")
    descripcion = models.CharField("Descripción", max_length=20)

    class Meta:
        managed = True
        db_table = 'sensor'
        
    def __str__(self):
        return self.descripcion
    
    
class TipoActuador(models.Model):
    id_tipo_actuador = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo_actuador'
        
    def __str__(self):
        return self.descripcion


class Actuador(models.Model):
    id_actuador = models.AutoField(primary_key=True)
    id_dispositivo_fk = models.ForeignKey(Dispositivo, 
                                          models.DO_NOTHING, 
                                          db_column='id_dispositivo_fk',
                                          verbose_name="Controlador")
    id_tipo_actuador_fk = models.ForeignKey('TipoActuador', 
                                            models.DO_NOTHING, 
                                            db_column='id_tipo_actuador_fk',
                                            verbose_name="Tipo de Actuador")
    descripcion = models.CharField("Descripci&oacute;n", max_length=20)

    class Meta:
        managed = True
        db_table = 'actuador'
        
    def __str__(self):
        return self.descripcion


class PublicacionActuador(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_actuador_fk = models.ForeignKey(Actuador, models.DO_NOTHING, db_column='id_actuador_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        managed = True
        db_table = 'publicacion_actuador'
        
    def __str__(self):
        return self.id_actuador_fk + " | " + self.fecha


class PublicacionSensor(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_sensor_fk = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='id_sensor_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'publicacion_sensor'
        
    def __str__(self):
        return self.id_sensor_fk + " | " + self.fecha
        