# Generated by Django 5.1.3 on 2024-11-07 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alumno_curso_maestro_asignacioncurso_curso_maestro_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='roll',
            field=models.CharField(default='Alumno', max_length=100),
        ),
        migrations.AddField(
            model_name='maestro',
            name='roll',
            field=models.CharField(default='Maestro', max_length=100),
        ),
    ]
