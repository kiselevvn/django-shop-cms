from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.serializers import ModelSerializer
from ..models import Cart


class CartSerializer(ModelSerializer):
    """
    Серилизатор записи в корзине
    """

    class Meta:
        model = Cart
        fields = [
            "count",
        ]


class UpdateСountProduct(RetrieveUpdateAPIView):
    """
    Обновление количества товара
    """

    serializer_class = CartSerializer
    queryset = Cart.objects.all()
