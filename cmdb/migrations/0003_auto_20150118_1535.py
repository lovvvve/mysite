# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0002_auto_20150118_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='department',
            field=models.CharField(max_length=30),
            preserve_default=True,
        ),
    ]
