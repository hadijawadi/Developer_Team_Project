# Generated by Django 5.1.3 on 2024-12-04 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_cart_app', '0010_usercart_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercart',
            name='product_name_special',
        ),
        migrations.AlterField(
            model_name='usercart',
            name='product_name',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]