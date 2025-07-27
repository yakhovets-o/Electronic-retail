from django.db import models
from django.utils import timezone


class Product(models.Model):
    """Product model for nodel"""

    name = models.CharField(max_length=255, verbose_name="Название")
    model = models.CharField(max_length=100, verbose_name="Модель")
    date_product_release = models.DateTimeField(default=timezone.now, verbose_name="Дата выхода")

    def __str__(self):
        return f"{self.name},  {self.model}, {self.date_product_release}"


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ['-date_product_release']
