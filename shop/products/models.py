from django.db import models
from PIL import Image


class Product(models.Model):
    SMARTPHONES = 'Смартфоны'
    NOTEBOOKS = 'Ноутбуки'
    PC = 'Персональные компьютеры'
    ACC = 'Аксессуары'

    CHOICE_GROUP = {
        (SMARTPHONES, 'Смартфоны'),
        (NOTEBOOKS, 'Ноутбуки'),
        (PC, 'Персональные компьютеры'),
        (ACC, 'Аксессуары'),
    }

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True, default=None)
    price = models.IntegerField(default=0)
    availability = models.BooleanField()
    group = models.CharField(max_length=25, choices=CHOICE_GROUP, default=SMARTPHONES)
    img = models.ImageField(default='no_image.png', upload_to='product_images')

    def __str__(self):
        return f'{self.name} {self.price}'

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    product = models.ForeignKey(Product, blank=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'Заказ № {self.product.name}'

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'
