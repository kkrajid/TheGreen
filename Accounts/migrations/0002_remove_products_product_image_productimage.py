# Generated by Django 4.1.7 on 2023-04-28 14:20

import Accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='product_image',
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=Accounts.models.getFileName)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.products')),
            ],
        ),
    ]
