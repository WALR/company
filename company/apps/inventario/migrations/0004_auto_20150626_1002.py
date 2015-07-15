# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inventario', '0003_auto_20150622_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('encargado', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creado', models.DateTimeField(auto_now_add=True)),
                ('modificado', models.DateTimeField(auto_now=True)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('telefono', models.PositiveIntegerField(null=True, blank=True)),
                ('email', models.EmailField(max_length=254, null=True, blank=True)),
                ('encargado', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='actualizado',
            new_name='modificado',
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='marca',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='barcode',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to=b'producto', blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='existencia',
            field=models.PositiveIntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ManyToManyField(to='inventario.Proveedor', blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='sucursal',
            field=models.ManyToManyField(to='inventario.Sucursal', blank=True),
        ),
    ]
