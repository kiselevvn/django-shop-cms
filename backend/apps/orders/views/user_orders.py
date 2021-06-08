from django.views.generic import View
from django.shortcuts import render
from ..models import Order
from django.shortcuts import redirect


class UserOrdersView(View):
    """
    Заказы пользователя
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        orders = Order.objects.filter(user=user)
        return render(request, "apps/users/profile.html", {"orders": orders})
