# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
                ('precio', models.DecimalField(max_digits=6, decimal_places=2)),
                ('existencia', models.PositiveIntegerField()),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
                ('categoria', models.ForeignKey(to='inventario.Categoria')),
            ],
        ),
    ]
