# Generated by Django 2.2.14 on 2021-11-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0047_discount_max_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='unit',
            field=models.CharField(choices=[('PERCENTAGE', 'percentage'), ('CURRENCY', 'currency')], default='PERCENTAGE', max_length=10, verbose_name='unit'),
        ),
        migrations.AlterField(
            model_name='discount',
            name='amount',
            field=models.PositiveSmallIntegerField(verbose_name='amount'),
        ),
        migrations.AddConstraint(
            model_name='discount',
            constraint=models.CheckConstraint(check=models.Q(('amount__gte', 0), ('amount__lte', 100), ('unit', 'PERCENTAGE')), name='percentage'),
        ),
    ]
