from django.db import models
from django.core.validators import MinValueValidator

from sales_networks.models.product import Product
from sales_networks.utils.created_updated_mixins import CreatedUpdatedMixins


class NetworkNode(CreatedUpdatedMixins, models.Model):
    """Retail network node model"""

    title = models.CharField(max_length=255, verbose_name="Название")
    # contacts
    email = models.EmailField(max_length=100, unique=True, verbose_name="Электронная почта")
    country = models.CharField(max_length=100, verbose_name="Страна")
    city = models.CharField(max_length=100, verbose_name="Город")
    street = models.CharField(max_length=100, verbose_name="Улица")
    house_number = models.CharField(max_length=50, verbose_name="Номер дома")

    product = models.ManyToManyField(Product, verbose_name="Продукт")
    supplier = models.ForeignKey("NetworkNode", on_delete=models.PROTECT, blank=True, verbose_name="Поставщик")

    debt = models.DecimalField(max_digits=20, decimal_places=2, default=.00, validators=[MinValueValidator(0)],
                               verbose_name="Задолженность")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Звено Сети"
        verbose_name_plural = "Звенья Сети"
        ordering = ["-created", "-debt", "title"]
