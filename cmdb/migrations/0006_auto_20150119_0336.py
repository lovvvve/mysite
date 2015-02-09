# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_server_ip_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='Ip_address',
            field=models.ForeignKey(to='cmdb.Ip_address'),
            preserve_default=True,
        ),
    ]
