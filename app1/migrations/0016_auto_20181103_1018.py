# Generated by Django 2.1.2 on 2018-11-03 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0015_auto_20181103_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='payment_status',
            field=models.CharField(choices=[('partpayment', 'PartPayment'), ('fullpayment', 'FullPayment')], max_length=100),
        ),
    ]
