# Generated by Django 4.2.2 on 2023-06-25 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_customer_address_order_total_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='total_amount',
            new_name='total_price',
        ),
    ]
