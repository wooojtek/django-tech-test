# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone', models.IntegerField()),
                ('company_name', models.CharField(max_length=20)),
                ('company_address', models.CharField(max_length=100)),
                ('company_number', models.IntegerField()),
                ('company_sector', models.CharField(max_length=20,
                                                    choices=[(b're', b'Retail'), (b'pf', b'Professional Services'),
                                                             (b'fd', b'Food & Drink'), (b'en', b'Entertainment')])),
                ('loan_amount', models.IntegerField()),
                ('loan_period', models.IntegerField()),
                ('loan_reason', models.TextField()),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
