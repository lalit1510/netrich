# Generated by Django 2.1.3 on 2018-11-04 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0022_auto_20181104_1048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='refrence',
            new_name='college',
        ),
    ]