# Generated by Django 4.2.2 on 2023-06-25 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Смартфоны', 'Смартфоны'), ('Ноутбуки', 'Ноутбуки'), ('Аксессуары', 'Аксессуары'), ('Персональные компьютеры', 'Персональные компьютеры')], default='Смартфоны', max_length=25),
        ),
    ]
