# Generated by Django 4.0 on 2022-02-19 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_price'),
        ('cart', '0004_cart_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='products',
            field=models.ManyToManyField(null=True, to='products.Products'),
        ),
    ]
