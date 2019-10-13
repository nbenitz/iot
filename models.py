# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actuador(models.Model):
    id_actuador = models.AutoField(primary_key=True)
    id_dispositivo_fk = models.ForeignKey('Dispositivo', models.DO_NOTHING, db_column='id_dispositivo_fk')
    id_tipo_actuador_fk = models.ForeignKey('TipoActuador', models.DO_NOTHING, db_column='id_tipo_actuador_fk')
    topic = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'actuador'


class Cultivo(models.Model):
    id_cultivo = models.AutoField(primary_key=True)
    id_sector_fk = models.ForeignKey('Sector', models.DO_NOTHING, db_column='id_sector_fk')
    id_tipo_cultivo_fk = models.ForeignKey('TipoCultivo', models.DO_NOTHING, db_column='id_tipo_cultivo_fk')
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'cultivo'


class Dispositivo(models.Model):
    id_dispositivo = models.AutoField(primary_key=True)
    id_invernadero_fk = models.ForeignKey('Invernadero', models.DO_NOTHING, db_column='id_invernadero_fk')
    id_cultivo_kf = models.ForeignKey(Cultivo, models.DO_NOTHING, db_column='id_cultivo_kf', blank=True, null=True)
    nombre = models.CharField(max_length=20)
    ip = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dispositivo'


class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'empresa'


class Invernadero(models.Model):
    id_invernadero = models.AutoField(primary_key=True)
    id_empresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa_fk')
    nombre = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=100, blank=True, null=True)
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invernadero'


class Produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)
    id_producto = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = False
        db_table = 'produccion'


class PublicacionActuador(models.Model):
    id_publicacion = models.AutoField(primary_key=True)
    id_actuador_fk = models.ForeignKey(Actuador, models.DO_NOTHING, db_column='id_actuador_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=3, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'publicacion_actuador'


class PublicacionSensor(models.Model):
    id_publicacion = models.PositiveIntegerField(primary_key=True)
    id_sensor_fk = models.ForeignKey('Sensor', models.DO_NOTHING, db_column='id_sensor_fk')
    fecha = models.DateTimeField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'publicacion_sensor'


class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    id_invernadero_fk = models.ForeignKey(Invernadero, models.DO_NOTHING, db_column='id_invernadero_fk')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'


class Sensor(models.Model):
    id_sensor = models.AutoField(primary_key=True)
    id_dispositivo_fk = models.ForeignKey(Dispositivo, models.DO_NOTHING, db_column='id_dispositivo_fk')
    id_tipo_sensor_fk = models.ForeignKey('TipoSensor', models.DO_NOTHING, db_column='id_tipo_sensor_fk')
    topic = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'sensor'


class TipoActuador(models.Model):
    id_tipo_actuador = models.AutoField(primary_key=True)
    descripcion = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_actuador'


class TipoCultivo(models.Model):
    id_tipo_cultivo = models.AutoField(primary_key=True)
    descripcion = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'tipo_cultivo'


class TipoSensor(models.Model):
    id_tipo_sensor = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'tipo_sensor'
