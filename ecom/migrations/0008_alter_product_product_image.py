# Generated by Django 4.2.2 on 2023-06-28 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0007_rename_shipping_charge_product_gst'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_image/'),
        ),
    ]
