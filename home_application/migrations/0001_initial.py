# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MultRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('multiplier', models.IntegerField(verbose_name=b'chengshu')),
                ('multiplicand', models.IntegerField(verbose_name=b'beichengshu')),
                ('mult_result', models.IntegerField(verbose_name=b'mult_result')),
            ],
        ),
    ]
