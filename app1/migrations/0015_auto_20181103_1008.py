# Generated by Django 2.1.2 on 2018-11-03 04:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0014_auto_20181023_0924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='fees',
            field=models.FloatField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Fees should be numeric value', regex='^\\d{4,5}$')]),
        ),
    ]
