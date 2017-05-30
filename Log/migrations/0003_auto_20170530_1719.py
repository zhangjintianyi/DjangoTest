# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Log', '0002_auto_20170528_2013'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '用户信息表', 'verbose_name_plural': '用户信息表'},
        ),
        migrations.AlterField(
            model_name='user',
            name='about_me',
            field=models.TextField(verbose_name='用户的自我描述', default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='confirmed',
            field=models.BooleanField(verbose_name='是否点击邮件确认', default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(verbose_name='用户邮箱', max_length=254, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='location',
            field=models.CharField(verbose_name='用户所在地', max_length=100, default=''),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(verbose_name='密码', max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(verbose_name='用户名', max_length=20),
        ),
        migrations.AlterModelTable(
            name='user',
            table='Users',
        ),
    ]
