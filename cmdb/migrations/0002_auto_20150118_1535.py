# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='backupowner',
        ),
        migrations.RemoveField(
            model_name='host',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='application',
            name='department',
            field=models.CharField(default=b'department', max_length=30),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ip_address',
            name='ip_address',
            field=models.CharField(unique=True, max_length=15),
            preserve_default=True,
        ),
    ]
