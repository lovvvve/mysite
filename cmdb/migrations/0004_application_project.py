# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0003_auto_20150118_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='project',
            field=models.CharField(default=b'peoject', max_length=30),
            preserve_default=True,
        ),
    ]
