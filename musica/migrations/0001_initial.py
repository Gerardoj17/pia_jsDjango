# Generated by Django 5.1.3 on 2024-11-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('te_gusta_la_pagina', models.CharField(max_length=2)),
                ('genero_musical', models.CharField(max_length=10)),
                ('frecuencia_escucha', models.CharField(max_length=15)),
                ('plataforma_utilizada', models.CharField(max_length=10)),
                ('aprender_mas_musica', models.CharField(max_length=2)),
            ],
        ),
    ]
