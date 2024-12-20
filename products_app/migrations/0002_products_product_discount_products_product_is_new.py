# Generated by Django 5.1.3 on 2024-11-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_discount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='product_is_new',
            field=models.BooleanField(default=True),
        ),
    ]
