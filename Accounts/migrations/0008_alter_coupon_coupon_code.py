# Generated by Django 4.1.7 on 2023-04-29 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_products_product_image_delete_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='coupon_code',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
