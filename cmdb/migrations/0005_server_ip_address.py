# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0004_application_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='Ip_address',
            field=models.ForeignKey(default=b'1', to='cmdb.Ip_address'),
            preserve_default=True,
        ),
    ]
