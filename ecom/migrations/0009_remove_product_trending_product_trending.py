# Generated by Django 4.2.2 on 2023-06-28 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0008_alter_product_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='trending',
        ),
        migrations.AddField(
            model_name='product',
            name='Trending',
            field=models.BooleanField(default=False, help_text='0-default,1-Trending'),
        ),
    ]
