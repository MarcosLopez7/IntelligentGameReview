# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-05 18:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calificacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ESRB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clasificacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_lanzamiento', models.DateField()),
                ('foto', models.ImageField(upload_to='images')),
                ('trailer', models.FileField(upload_to='videos')),
                ('resumen', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=12)),
                ('calificacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Calificacion')),
                ('esrb', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.ESRB')),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Nombre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Plataforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numJugadores', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='general',
            name='genero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Genero'),
        ),
        migrations.AddField(
            model_name='general',
            name='nombre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Nombre'),
        ),
        migrations.AddField(
            model_name='general',
            name='plataforma',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Plataforma'),
        ),
        migrations.AddField(
            model_name='general',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Player'),
        ),
        migrations.AddField(
            model_name='general',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reviews.Publisher'),
        ),
    ]
