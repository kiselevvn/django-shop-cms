from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    OrderMixin,
)


class GroupCategories(OrderMixin, models.Model):
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

    class Meta:
        verbose_name = _("Группа категорий")
        verbose_name_plural = _("Группы категорий")

    def __str__(self):
        return self.name
