# Generated by Django 3.1.2 on 2020-10-10 04:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublicacionControlador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=0, max_digits=1)),
                ('controlador', models.ForeignKey(db_column='controlador', on_delete=django.db.models.deletion.DO_NOTHING, to='dispositivo.dispositivo')),
            ],
            options={
                'db_table': 'publicacion_controlador',
            },
        ),
    ]
