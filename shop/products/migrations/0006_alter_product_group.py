# Generated by Django 4.2.2 on 2023-06-25 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_group'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='group',
            field=models.CharField(choices=[('Ноутбуки', 'Ноутбуки'), ('Смартфоны', 'Смартфоны'), ('Аксессуары', 'Аксессуары'), ('Персональные компьютеры', 'Персональные компьютеры')], default='Смартфоны', max_length=25),
        ),
    ]
