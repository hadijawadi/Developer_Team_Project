# Generated by Django 5.1.3 on 2024-11-22 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_products_product_discount_products_product_is_new'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]