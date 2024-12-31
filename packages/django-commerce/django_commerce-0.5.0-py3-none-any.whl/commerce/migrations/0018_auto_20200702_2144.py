# Generated by Django 2.2.4 on 2020-07-02 19:44

from django.db import migrations, models
import modeltrans.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0023_invoice_related_invoices'),
        ('commerce', '0017_purchaseditem_option'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoices',
            field=models.ManyToManyField(blank=True, related_name='orders', to='invoicing.Invoice', verbose_name='invoices'),
        ),
        migrations.AlterField(
            model_name='option',
            name='i18n',
            field=modeltrans.fields.TranslationField(fields=('title', 'slug'), required_languages=(), virtual_fields=True),
        ),
    ]
