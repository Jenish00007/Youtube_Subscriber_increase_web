# Generated by Django 4.2.2 on 2023-08-31 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0018_transation'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Channelstatus',
            field=models.CharField(default='', max_length=100),
        ),
    ]
