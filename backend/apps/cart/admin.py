from .models import Cart
from django.contrib import admin


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    Общая корзина
    """

    list_display = (
        "product",
        "count",
    )

    list_filter = ("user",)
