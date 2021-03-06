# Generated by Django 2.1.2 on 2018-10-20 13:26

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('email', models.CharField(max_length=256, unique=True)),
                ('mobile', models.IntegerField(unique=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Length has to be 10', regex='^[6-9]\\d{9}$')])),
                ('city', models.CharField(max_length=256)),
                ('refrence', models.CharField(max_length=256)),
                ('enquiary_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fees', models.CharField(blank=True, max_length=5, null=True, validators=[django.core.validators.RegexValidator(code='Invalid number', message='Fees should be numeric value', regex='^\\d{4,5}$')])),
                ('fees_date', models.DateTimeField(blank=True, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Course')),
            ],
        ),
    ]
