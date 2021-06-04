from django.db import models
from django.utils.translation import gettext as _
from apps.services.models import (
    DateCreatedMixin,
    DateUpdatedMixin,
)


class Order(DateUpdatedMixin, DateCreatedMixin, models.Model):
    """
    Заказ
    """

    user = models.ForeignKey(
        "users.User",
        verbose_name=_("Пользователь"),
        on_delete=models.CASCADE,
        related_name="cart",
    )
    comment = models.TextField(
        verbose_name=_("Описание"), blank=True, null=True
    )

    @property
    def price(self):
        """
        Сумма заказа
        """
        price = 0
        # TODO: Сервис подсчета суммы заказа
        print(self.positions)
        return price

    class Meta:
        verbose_name = _("Заказ")
        verbose_name_plural = _("Заказы")
        ordering = ["-date_created"]

    # def __str__(self):
    #     return f"{self.name} - {self.email} на сумму {self.price}"
