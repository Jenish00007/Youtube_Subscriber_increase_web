# Generated by Django 4.2.2 on 2023-06-25 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0003_product_latest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='trending',
            field=models.BooleanField(default=False, help_text='0-default,1-trending'),
        ),
    ]
