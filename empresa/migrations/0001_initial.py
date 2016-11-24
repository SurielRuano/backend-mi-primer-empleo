# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 20:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('egresados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('street', models.CharField(max_length=100)),
                ('colony', models.CharField(max_length=100)),
                ('cpostal', models.IntegerField()),
                ('adress_visits', models.TextField()),
                ('tel', models.CharField(max_length=10)),
                ('fax', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('replegal', models.CharField(max_length=40)),
                ('start_date', models.DateField()),
                ('total_number_workes', models.IntegerField()),
                ('giro', models.CharField(max_length=40)),
                ('registry_date', models.DateField()),
                ('name_project_manager', models.CharField(max_length=60)),
                ('puesto', models.CharField(max_length=60)),
                ('rfc', models.CharField(max_length=20)),
                ('acteconomica', models.CharField(max_length=250)),
                ('products_services', models.TextField()),
                ('name_project', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('size', models.CharField(max_length=10)),
                ('clasificacion', models.CharField(max_length=10)),
                ('sectores', models.IntegerField()),
                ('sector', models.CharField(max_length=10)),
                ('rango_trab', models.CharField(max_length=60)),
                ('acceso', models.CharField(max_length=60)),
                ('extension', models.CharField(max_length=60)),
                ('rfc_imagen', models.ImageField(upload_to='rfc_imagen')),
                ('identificacion', models.CharField(max_length=60)),
                ('identificacion_tutor', models.CharField(max_length=60)),
                ('comprobante', models.CharField(max_length=60)),
                ('carta', models.CharField(max_length=60)),
                ('pagina', models.CharField(max_length=60)),
                ('ubucacion', models.TextField()),
                ('croquis', models.CharField(max_length=60)),
                ('emailreproy', models.EmailField(max_length=254)),
                ('validada', models.IntegerField()),
                ('etapa', models.CharField(max_length=60)),
                ('carpeta', models.IntegerField()),
                ('administra', models.IntegerField()),
                ('visto', models.IntegerField()),
                ('id_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Expediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('observacion', models.CharField(max_length=400)),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.BusinessModel')),
                ('id_egresado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='egresados.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipio', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=5)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_egresado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspirante', to='egresados.Egresado')),
            ],
        ),
        migrations.CreateModel(
            name='Vacante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puesto_solicitante', models.CharField(max_length=80)),
                ('activades', models.TextField()),
                ('dias', models.TextField()),
                ('horario_entrada', models.CharField(max_length=50)),
                ('horario_entrada_sabado', models.CharField(blank=True, max_length=50, null=True)),
                ('horario_salida', models.CharField(max_length=50)),
                ('horario_salida_sabado', models.CharField(blank=True, max_length=50, null=True)),
                ('fecha_alta', models.CharField(max_length=50)),
                ('fecha_asignado', models.CharField(max_length=50)),
                ('vacante_activa', models.BooleanField(default=True)),
                ('id_egresado', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vacante', to='egresados.Egresado')),
                ('id_empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vacante', to='empresa.BusinessModel')),
            ],
        ),
        migrations.AddField(
            model_name='solicitud',
            name='id_vacante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aspirante', to='empresa.Vacante'),
        ),
        migrations.AddField(
            model_name='expediente',
            name='vacante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Vacante'),
        ),
        migrations.AddField(
            model_name='businessmodel',
            name='municipio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.Municipio'),
        ),
    ]
