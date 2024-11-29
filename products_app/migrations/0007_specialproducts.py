# Generated by Django 5.1.3 on 2024-11-29 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory_app', '0005_remove_catagory_cata_products'),
        ('products_app', '0006_products_product_catagory'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=250)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField(blank=True, max_length=500, null=True)),
                ('product_first_image', models.ImageField(upload_to='products/Images')),
                ('product_second_image', models.ImageField(upload_to='products/Images')),
                ('product_third_image', models.ImageField(blank=True, null=True, upload_to='products/Images')),
                ('prodcut_fourth_image', models.ImageField(blank=True, null=True, upload_to='products/Images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('product_catagory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catagory_app.catagory')),
            ],
        ),
    ]