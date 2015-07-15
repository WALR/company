# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0004_auto_20150626_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='proveedor',
        ),
        migrations.AddField(
            model_name='producto',
            name='proveedor',
            field=models.ForeignKey(default=1, blank=True, to='inventario.Proveedor'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='producto',
            name='sucursal',
        ),
        migrations.AddField(
            model_name='producto',
            name='sucursal',
            field=models.ForeignKey(default=1, blank=True, to='inventario.Sucursal'),
            preserve_default=False,
        ),
    ]
