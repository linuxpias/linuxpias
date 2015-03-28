# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('autor', models.CharField(max_length=50)),
                ('contenido_pri', models.TextField(verbose_name=b'contenido principal')),
                ('contenido_ext', models.TextField(verbose_name=b'contenido extendido')),
                ('imagen_pri', models.ImageField(upload_to=b'', verbose_name=b'imagen principal')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ArticuloTipo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Tipo de articulo',
                'verbose_name_plural': 'Tipos de articulo',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Etiqueta',
                'verbose_name_plural': 'Etiquetas',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='articulo',
            name='categoria',
            field=models.ForeignKey(to='articulos.ArticuloTipo'),
            preserve_default=True,
        ),
    ]
