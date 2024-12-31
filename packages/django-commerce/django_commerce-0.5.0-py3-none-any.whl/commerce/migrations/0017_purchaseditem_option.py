# Generated by Django 2.2.4 on 2020-07-02 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0016_auto_20200702_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchaseditem',
            name='option',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='commerce.Option'),
        ),
    ]
