# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0006_auto_20150119_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='hypervisor',
            name='serial_number',
            field=models.ForeignKey(default=2, to='cmdb.Server'),
            preserve_default=True,
        ),
    ]
