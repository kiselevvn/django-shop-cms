from django.db import models
from django.utils.translation import gettext as _


class Cart(models.Model):
    """
    Модель корзины
    """

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="products_in_cart",
    )
    product = models.ForeignKey(
        "products.Product", verbose_name=_("Товар"), on_delete=models.CASCADE
    )
    count = models.PositiveIntegerField(_("Количество товара"))

    class Meta:
        verbose_name = _("Товар в корзине")
        verbose_name_plural = _("Товары в корзинах")
        ordering = ["-user"]
