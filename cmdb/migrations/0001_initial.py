# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=30)),
                ('backupowner', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=10)),
                ('mobile_phone', models.CharField(max_length=11)),
                ('phone_ext', models.CharField(max_length=5)),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=30)),
                ('appname', models.ForeignKey(to='cmdb.Application')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Hypervisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hypervisor_hostname', models.CharField(max_length=30)),
                ('vm_number', models.SmallIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ip_address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip_address', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_hypervisor', models.BooleanField(default=False)),
                ('device_model', models.CharField(max_length=50)),
                ('serial_number', models.CharField(unique=True, max_length=30)),
                ('UUID', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VM',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('UUID', models.CharField(max_length=30)),
                ('hypervisor_ip', models.ForeignKey(to='cmdb.Hypervisor')),
                ('vm_ip', models.ForeignKey(to='cmdb.Ip_address')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='hypervisor',
            name='hypervisor_ip',
            field=models.ForeignKey(to='cmdb.Ip_address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='private_ip',
            field=models.ForeignKey(to='cmdb.Ip_address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='host',
            name='serial_number',
            field=models.ForeignKey(to='cmdb.Server'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='application',
            name='owner',
            field=models.ForeignKey(to='cmdb.Contacts'),
            preserve_default=True,
        ),
    ]
