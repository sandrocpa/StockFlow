# Generated by Django 4.2.7 on 2023-11-10 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_products', '0007_alter_qtdproduto_id_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='qtdproduto',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='QtdProduto',
        ),
    ]
