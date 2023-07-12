from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=12, blank=True)
    message = models.TextField()

    def __str__(self):
        return f'{self.id} {self.email} {self.name} {self.phone} {self.message}'

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатели'
