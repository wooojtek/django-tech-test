# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('borrower', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
