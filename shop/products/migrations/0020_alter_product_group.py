# Generated by Django 4.2.2 on 2023-07-06 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Ноутбуки', 'Ноутбуки'), ('Аксессуары', 'Аксессуары'), ('Смартфоны', 'Смартфоны'), ('Персональные компьютеры', 'Персональные компьютеры')], default='Смартфоны', max_length=25),
        ),
    ]
