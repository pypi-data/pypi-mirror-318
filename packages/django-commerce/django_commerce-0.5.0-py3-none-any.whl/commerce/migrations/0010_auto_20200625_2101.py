# Generated by Django 2.2.4 on 2020-06-25 19:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0009_purchaseditem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseditem',
            name='content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType'),
        ),
    ]
