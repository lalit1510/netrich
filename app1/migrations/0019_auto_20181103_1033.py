# Generated by Django 2.1.3 on 2018-11-03 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0018_auto_20181103_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_status',
            field=models.CharField(choices=[('Enquiary', 'Enquiary'), ('Registered', 'Register')], max_length=25),
        ),
    ]
