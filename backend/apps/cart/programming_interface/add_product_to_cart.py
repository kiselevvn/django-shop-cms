from rest_framework.generics import CreateAPIView
from rest_framework.serializers import (
    ModelSerializer,
)
from ..models import Cart


class CartSerializer(ModelSerializer):
    """
    Серилизатор записи в корзине
    """

    class Meta:
        model = Cart
        fields = ["product", "count"]

    def create(self, validated_data):
        user = self.context["request"].user
        cart = Cart.objects.create(user=user, **validated_data)
        return cart


class AddProductToCart(CreateAPIView):
    """
    Добавление товара в корзину
    """

    serializer_class = CartSerializer
    queryset = Cart.objects.all()
