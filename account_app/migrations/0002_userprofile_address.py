# Generated by Django 5.1.3 on 2024-11-27 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
