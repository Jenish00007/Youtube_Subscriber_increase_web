from django.db import migrations, models
import ecom.models

class Migration(migrations.Migration):

    dependencies = [
        ('ecom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catagory',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='catagory_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(blank=True, null=True, upload_to='product_images/'),
        ),
    ]
