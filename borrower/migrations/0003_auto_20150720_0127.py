# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('borrower', '0002_auto_20150720_0125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrower',
            name='company_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='loan_amount',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='loan_period',
            field=models.IntegerField(null=True),
        ),
    ]
