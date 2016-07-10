# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-06-19 08:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atmb', '0004_auto_20160612_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='down_lead_line',
            name='cable_quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='1米'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='check_result',
            field=models.IntegerField(blank=True, choices=[(0, '合格'), (1, '不合格')], null=True, verbose_name='检查结论'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='distance_away_cable',
            field=models.IntegerField(blank=True, choices=[(0, '>='), (1, '<')], null=True, verbose_name='与电缆水平距离'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='mode',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='形式'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='resistance',
            field=models.IntegerField(blank=True, null=True, verbose_name='接地电阻'),
        ),
        migrations.AlterField(
            model_name='down_lead_line',
            name='spec',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='规格'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='check_result',
            field=models.IntegerField(blank=True, choices=[(0, '合格'), (1, '不合格')], null=True, verbose_name='检查结论'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='construction_date',
            field=models.IntegerField(blank=True, null=True, verbose_name='建设日期'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='material',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='主要材料规格'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='mode',
            field=models.IntegerField(blank=True, choices=[(0, '自然接地体'), (1, '人工接地体'), (2, '联合接地装置')], null=True, verbose_name='形式'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='位置'),
        ),
        migrations.AlterField(
            model_name='earth_device',
            name='resistance',
            field=models.IntegerField(blank=True, null=True, verbose_name='接地电阻'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='check_result',
            field=models.IntegerField(blank=True, choices=[(0, '合格'), (1, '不合格')], null=True, verbose_name='检查结论'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='install_date',
            field=models.DateField(blank=True, null=True, verbose_name='安装时间'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='light_device',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='接闪装置'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='位置,高度,覆盖'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='quantity',
            field=models.IntegerField(blank=True, null=True, verbose_name='数量'),
        ),
        migrations.AlterField(
            model_name='lightning_receptor',
            name='resistance',
            field=models.IntegerField(blank=True, null=True, verbose_name='接地电阻'),
        ),
        migrations.AlterField(
            model_name='thunder_external_protect',
            name='memo',
            field=models.CharField(max_length=50, verbose_name='备注'),
        ),
    ]
