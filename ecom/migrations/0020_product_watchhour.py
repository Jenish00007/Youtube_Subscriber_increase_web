# Generated by Django 4.2.2 on 2023-08-31 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0019_product_channelstatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Watchhour',
            field=models.CharField(default='', max_length=100),
        ),
    ]