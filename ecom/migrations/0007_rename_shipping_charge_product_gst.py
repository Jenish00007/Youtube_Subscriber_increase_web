# Generated by Django 4.2.2 on 2023-06-26 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0006_product_shipping_charge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='shipping_charge',
            new_name='gst',
        ),
    ]
