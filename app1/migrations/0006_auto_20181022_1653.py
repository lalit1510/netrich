# Generated by Django 2.1.2 on 2018-10-22 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20181020_1915'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-fees_date', '-enquiary_date')},
        ),
    ]