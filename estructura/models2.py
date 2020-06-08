# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = True` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Empresa(models.Model):
    id_empresa = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    ruc = models.CharField(max_length=15, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    ciudad = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'empresa'
    
    def __str__(self):
        return self.nombre


class Invernadero(models.Model):
    id_invernadero = models.AutoField(primary_key=True)
    id_empresa_fk = models.ForeignKey(Empresa, models.DO_NOTHING, db_column='id_empresa_fk')
    nombre = models.CharField(max_length=50)
    caracteristicas = models.CharField(max_length=100, blank=True, null=True)
    foto = models.TextField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'invernadero'
        
    def __str__(self):
        return self.nombre
        
class Sector(models.Model):
    id_sector = models.AutoField(primary_key=True)
    id_invernadero_fk = models.ForeignKey(Invernadero, models.DO_NOTHING, db_column='id_invernadero_fk')
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sector'
        
    def __str__(self):
        return self.nombre
        
        
class TipoCultivo(models.Model):
    id_tipo_cultivo = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'tipo_cultivo'
        
    def __str__(self):
        return self.descripcion
        
        
class Cultivo(models.Model):
    id_cultivo = models.AutoField(primary_key=True)
    id_sector_fk = models.ForeignKey('Sector', models.DO_NOTHING, db_column='id_sector_fk')
    id_tipo_cultivo_fk = models.ForeignKey('TipoCultivo', models.DO_NOTHING, db_column='id_tipo_cultivo_fk')
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'cultivo'
        
    def __str__(self):
        return self.descripcion
        
        
"""      
class Produccion(models.Model):
    id_produccion = models.AutoField(primary_key=True)
    id_producto = models.PositiveIntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()

    class Meta:
        managed = True
        db_table = 'produccion'
"""


