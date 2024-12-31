# Generated by Django 2.2.4 on 2020-07-07 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0011_auto_20190418_0137'),
        ('commerce', '0024_auto_20200707_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditem',
            name='files',
            field=models.ManyToManyField(blank=True, to='filer.File', verbose_name='files'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='billing_street',
            field=models.CharField(max_length=200, verbose_name='street and number'),
        ),
    ]
