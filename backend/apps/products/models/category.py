from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    OrderMixin,
)


class Category(OrderMixin, models.Model):
    """
    Категория товара
    """

    name = models.CharField(verbose_name=_("Наименование"), max_length=255)
    description = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )
    is_published = models.BooleanField(
        verbose_name=_("Категория опубликована"), default=False
    )
    group_categories = models.ForeignKey(
        "products.GroupCategories",
        verbose_name=_("Группа"),
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="categories",
    )

    @property
    def count_products(self):
        return len(self.products.filter())

    class Meta:
        verbose_name = _("Категория товара")
        verbose_name_plural = _("Категории товара")

    def __str__(self):
        return self.name
