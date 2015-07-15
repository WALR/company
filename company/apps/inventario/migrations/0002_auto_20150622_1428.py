# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='precio',
            new_name='precioVenta',
        ),
        migrations.AddField(
            model_name='producto',
            name='precioCompra',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='precioPorMayor',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
