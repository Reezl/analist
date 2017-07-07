# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='image',
            field=models.ImageField(null=True, upload_to='categorias/images', blank=True, verbose_name='Imagem'),
        ),
    ]
