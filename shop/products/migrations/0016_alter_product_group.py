# Generated by Django 4.2.2 on 2023-07-03 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Аксессуары', 'Аксессуары'), ('Ноутбуки', 'Ноутбуки'), ('Смартфоны', 'Смартфоны'), ('Персональные компьютеры', 'Персональные компьютеры')], default='Смартфоны', max_length=25),
        ),
    ]
