# Generated by Django 5.1.3 on 2024-11-26 12:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagory_app', '0003_alter_catagory_cata_products'),
        ('products_app', '0005_alter_products_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='catagory',
            name='cata_products',
        ),
        migrations.AddField(
            model_name='catagory',
            name='cata_products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products_app.products'),
        ),
    ]
