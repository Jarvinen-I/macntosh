# Generated by Django 4.2.2 on 2023-07-06 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Смартфоны', 'Смартфоны'), ('Ноутбуки', 'Ноутбуки'), ('Персональные компьютеры', 'Персональные компьютеры'), ('Аксессуары', 'Аксессуары')], default='Смартфоны', max_length=25),
        ),
    ]
