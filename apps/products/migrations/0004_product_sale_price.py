# Generated by Django 4.2.1 on 2023-05-20 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_in_progress_quantity_product_quantity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sale_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=7),
        ),
    ]
