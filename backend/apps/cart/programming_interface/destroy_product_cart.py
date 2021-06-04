from rest_framework.generics import RetrieveDestroyAPIView
from ..models import Cart


class DestroyProductCart(RetrieveDestroyAPIView):
    """
    Удаление товара из корзины
    """

    queryset = Cart.objects.all()
