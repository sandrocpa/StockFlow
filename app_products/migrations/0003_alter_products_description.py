# Generated by Django 4.2.7 on 2023-11-10 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0002_alter_products_ncm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='description',
            field=models.TextField(max_length=255),
        ),
    ]
