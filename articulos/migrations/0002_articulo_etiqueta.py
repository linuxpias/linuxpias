# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='etiqueta',
            field=models.ManyToManyField(to='articulos.Etiqueta'),
            preserve_default=True,
        ),
    ]
