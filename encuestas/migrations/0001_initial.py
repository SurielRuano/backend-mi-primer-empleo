# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_captura', models.DateField(auto_now=True)),
                ('aporte', models.CharField(max_length=150)),
                ('viade_informacion', models.CharField(max_length=100)),
                ('act_desemp', models.CharField(max_length=100)),
                ('capacitacion', models.CharField(max_length=200)),
                ('apoyo_extra', models.TextField()),
                ('propuesta', models.TextField()),
                ('contratado', models.BooleanField(default=True)),
                ('motivo_no_contratacion', models.TextField()),
                ('fecha_contrato', models.DateField(auto_now=True)),
                ('salario', models.FloatField()),
                ('evaluacion_experiencia', models.CharField(max_length=200)),
                ('expectativas', models.TextField()),
                ('mejora_programa', models.TextField()),
                ('mejora_empresa', models.TextField()),
                ('mejora_institucion', models.TextField()),
                ('conocimientos', models.TextField()),
                ('entrevista', models.TextField()),
                ('oferta', models.TextField()),
                ('lugar', models.TextField()),
                ('id_sedeco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='encuesta', to='usuarios.Sedeco')),
            ],
        ),
    ]
