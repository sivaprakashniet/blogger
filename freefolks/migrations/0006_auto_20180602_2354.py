# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-03 06:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('freefolks', '0005_auto_20180602_2334'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='transaction',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name=b'Transaction date'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='bank_name',
            field=models.CharField(choices=[('axis', 'Axis Bank'), ('citi', 'Citi Bank'), ('hdfc', 'HDFC Bank')], max_length=50, verbose_name=b'Select your bank'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name=b'Transaction amount'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('credit', 'Credited to account'), ('debit', 'Debited from account')], max_length=50, verbose_name=b'Transaction type'),
        ),
    ]
