# Generated by Django 3.1.2 on 2020-11-02 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dispositivo', '0004_logs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publicacionactuador',
            name='retain',
        ),
        migrations.RemoveField(
            model_name='publicacioncontrolador',
            name='retain',
        ),
        migrations.RemoveField(
            model_name='publicacionsensor',
            name='retain',
        ),
    ]
