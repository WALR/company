# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20150622_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.ForeignKey(blank=True, to='inventario.Marca', null=True),
        ),
    ]
