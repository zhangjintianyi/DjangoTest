# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_me',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, default=None),
        ),
        migrations.AddField(
            model_name='user',
            name='location',
            field=models.CharField(max_length=100, default=None),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=50),
        ),
    ]
